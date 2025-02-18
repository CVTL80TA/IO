import hashlib
import os

import whisper
from faster_whisper.utils import _MODELS as FW_MODELS
from huggingface_hub import HfApi
from huggingface_hub.file_download import repo_folder_name

from speech_translate.ui.custom.download import whisper_download_with_progress_gui, faster_whisper_download_with_progress_gui


# donwload function
def download_model(model_key, root_win, cancel_func=None, after_func=None, download_root=None, use_faster_whisper=False):
    """Download a model from the official model repository

    Parameters
    ----------
    model_key : str
        one of the official model keys
    download_root: str
        path to download the model files; by default, it uses "~/.cache/whisper"
    in_memory: bool
        whether to preload the model weights into host memory

    Returns
    -------
    model_bytes : bytes
        the model checkpoint as a byte string
    """
    if download_root is None:
        download_root = get_default_download_root()

    model_id = whisper._MODELS[model_key] if not use_faster_whisper else FW_MODELS[model_key]

    # call different download function
    if not use_faster_whisper:
        return whisper_download_with_progress_gui(root_win, model_key, model_id, download_root, cancel_func, after_func)
    else:
        return faster_whisper_download_with_progress_gui(root_win, model_key, model_id, download_root, after_func)


# verify downloaded model sha
def verify_model_whisper(model_key, download_root=None):
    """Verify the SHA256 checksum of a downloaded model

    Parameters
    ----------
    model_key : str
        one of the official model names listed by `whisper.available_models()`
    download_root: str
        path to download the model files; by default, it uses "~/.cache/whisper"

    Returns
    -------
    bool
        True if the model is already downloaded
    """
    if download_root is None:
        download_root = get_default_download_root()

    if model_key not in whisper._MODELS:
        raise RuntimeError(f"Model {model_key} not found; available models = {whisper.available_models()}")

    model_file = os.path.join(download_root, model_key + ".pt")
    if not os.path.exists(model_file):
        return False

    expected_sha256 = whisper._MODELS[model_key].split("/")[-2]

    model_bytes = open(model_file, "rb").read()
    return hashlib.sha256(model_bytes).hexdigest() == expected_sha256


def verify_model_faster_whisper(model_key: str, cache_dir) -> bool:
    """Verify downloaded faster whisper model, more complex than checking whisper model because the model is downloaded from huggingface hub

    Parameters
    ----------
    model_key : str
        The key of the model
    cache_dir : _type_
        The cache directory

    Returns
    -------
    bool
        True if the model is already downloaded

    Raises
    ------
    ValueError
        If the model key is invalid
    """
    repo_id = FW_MODELS.get(model_key)
    if repo_id is None:
        raise ValueError("Invalid model size '%s', expected one of: %s" % (model_key, ", ".join(FW_MODELS.keys())))

    storage_folder = os.path.join(cache_dir, repo_folder_name(repo_id=repo_id, repo_type="model"))

    api = HfApi()
    repo_info = api.repo_info(repo_id=repo_id, repo_type="model")
    assert repo_info.sha is not None, "Repo info returned from server must have a revision sha."

    commit_hash = repo_info.sha
    snapshot_folder = os.path.join(storage_folder, "snapshots", commit_hash)
    blob_folder = os.path.join(storage_folder, "blobs")

    if not os.path.exists(snapshot_folder):
        return False

    # check if blob contain any .incomplete file or .lock file
    # meaning that the download is not finished
    for _root, _dirs, files in os.walk(blob_folder):
        for file in files:
            if file.endswith(".incomplete") or file.endswith(".lock"):
                return False

    # should be safe to assume that model is downloaded
    return True


# get default download root
def get_default_download_root():
    """Get the default download root

    Returns
    -------
    str
        the default download root
    """
    return os.getenv("XDG_CACHE_HOME", os.path.join(os.path.expanduser("~"), ".cache", "whisper"))
