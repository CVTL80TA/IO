"""
Read this first about ttk style:

- Good questions on ttk style
https://stackoverflow.com/questions/48517660/questions-on-using-ttk-style

- ttk style simple example
https://coderslegacy.com/python/tkinter-ttk-style/

- Get ttk style options
https://stackoverflow.com/questions/45389166/how-to-know-all-style-options-of-a-ttk-widget

"""
import os
import tkinter as tk
from tkinter import ttk, TclError

from loguru import logger

from speech_translate.globals import gc, sj
from speech_translate._path import dir_theme
from speech_translate.ui.custom.message import mbox

theme_list = ["sun-valley-light", "sun-valley-dark"]


def set_ui_style(theme: str, root=None):
    success = False
    try:
        logger.debug("Setting theme: %s", theme)
        set_theme(theme)
        success = True
    except Exception as e:
        logger.exception(e)
        logger.debug("Setting theme failed, converting back to default native theme")
        mbox("Error", f"Failed to set `{theme}` theme, converting back to default native theme", 2, root)
        theme = gc.native_theme
        set_theme(theme)
        sj.save_key("theme", theme)

    # -----------------------
    assert gc.style is not None
    # Global style
    if "light" in theme.lower() or theme == gc.native_theme:
        logger.debug("Setting custom light theme style")
        gc.style.configure("Bottom.TFrame", background="#f0f0f0")
        gc.style.configure("Brighter.TFrame", background="#ffffff")
        gc.style.configure("BrighterTFrameBg.TLabel", background="#ffffff")
        gc.style.configure("Darker.TFrame", background="#000000")
    else:
        logger.debug("Setting custom dark theme style")
        gc.style.configure("Bottom.TFrame", background="#1e1e1e")
        gc.style.configure("Brighter.TFrame", background="#2e2e2e")
        gc.style.configure("BrighterTFrameBg.TLabel", background="#2e2e2e")
        gc.style.configure("Darker.TFrame", background="#bdbdbd")

    return success


def get_root() -> tk.Tk:
    assert gc.mw is not None
    return gc.mw.root


def get_style() -> ttk.Style:
    assert gc.style is not None
    return gc.style


def init_theme():
    dir_theme_list = [
        name for name in os.listdir(dir_theme) if os.path.isdir(os.path.join(dir_theme, name))
    ]  # only if a dir

    # filter path list by making sure that the dir name contains .tcl with the same name as the dir
    dir_theme_list = [dir for dir in dir_theme_list if dir + ".tcl" in os.listdir(os.path.join(dir_theme, dir))]

    for dir in dir_theme_list:
        path = os.path.abspath(os.path.join(dir_theme, dir, (dir + ".tcl")))
        theme_list.append(dir)

        try:
            get_root().tk.call("source", str(path))
        except AttributeError as e:
            logger.exception(e)


def get_current_theme() -> str:
    theme = get_root().tk.call("ttk::style", "theme", "use")

    return theme


def get_theme_list():
    real_theme_list = list(get_root().tk.call("ttk::style", "theme", "names"))

    theme = theme_list.copy()
    theme.extend(real_theme_list)
    theme = list(dict.fromkeys(theme))  # remove dupe after extend

    return theme


def set_theme(theme: str):
    real_theme_list = list(get_root().tk.call("ttk::style", "theme", "names"))
    real_theme_list.extend(theme_list)
    if theme not in real_theme_list:
        raise Exception("not a valid theme name: {}".format(theme))

    try:
        get_style().theme_use(theme)
        get_root().tk.call("set_theme", theme)
    except TclError as e:
        logger.exception(e)
