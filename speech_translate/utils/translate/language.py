from ..helper import up_first_case
from whisper.tokenizer import TO_LANGUAGE_CODE

# List of whisper languages convert fromm the keys of TO_LANGUAGE_CODE
whisper_compatible = list(TO_LANGUAGE_CODE.keys())

# List of supported languages by Google TL
google_lang = {
    "auto detect": "auto",
    "afrikaans": "af",
    "albanian": "sq",
    "amharic": "am",
    "arabic": "ar",
    "armenian": "hy",
    "azerbaijani": "aze_cyrl",
    "basque": "eu",
    "belarusian": "be",
    "bengali": "bn",
    "bosnian": "bs",
    "bulgarian": "bg",
    "burmese": "my",
    "catalan:valencian": "cat",
    "cebuano": "ceb",
    "chinese": "zh-CN",
    "chinese traditional": "zh-TW",
    "corsican": "co",
    "czech": "ces",
    "danish": "da",
    "dutch": "nl",
    "english": "en",
    "esperanto": "eo",
    "estonian": "et",
    "filipino (old-tagalog)": "tl",
    "finnish": "fi",
    "french": "fr",
    "galician": "gl",
    "georgian": "ka",
    "german": "de",
    "greek": "el",
    "gujarati": "gu",
    "haitian": "ht",
    "hebrew": "iw",
    "hindi": "hi",
    "hungarian": "hu",
    "icelandic": "is",
    "indonesian": "id",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "javanese": "jw",
    "kannada": "kn",
    "kazakh": "kk",
    "khmer": "km",
    "korean": "ko",
    "korean vertical": "ko",
    "kurdish": "ku",
    "lao": "lo",
    "latin": "la",
    "latvian": "lv",
    "lithuanian": "lt",
    "luxembourgish": "lb",
    "macedonian": "mk",
    "malay": "ms",
    "malayalam": "ml",
    "maltese": "mt",
    "maori": "mi",
    "marathi": "mr",
    "mongolian": "mn",
    "nepali": "ne",
    "norwegian": "no",
    "persian": "fa",
    "polish": "pl",
    "portuguese": "pt",
    "punjabi": "pa",
    "romanian": "ro",
    "russian": "ru",
    "serbian": "sr",
    "spanish": "es",
    "sundanese": "su",
    "swahili": "sw",
    "swedish": "sv",
    "tajik": "tg",
    "tamil": "ta",
    "tatar": "tt",
    "telugu": "te",
    "thai": "th",
    "turkish": "tr",
    "ukrainian": "uk",
    "urdu": "ur",
    "uzbek": "uz",
    "vietnamese": "vi",
    "welsh": "cy",
    "yiddish": "yi",
    "yoruba": "yo",
}

# List of supported languages by libreTranslate
libre_lang = {
    "auto detect": "auto",
    "arabic": "ar",
    "chinese": "zh",
    "dutch": "nl",
    "english": "en",
    "finnish": "fi",
    "french": "fr",
    "german": "de",
    "hindi": "hi",
    "hungarian": "hu",
    "indonesian": "id",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "korean": "ko",
    "polish": "pl",
    "portuguese": "pt",
    "russian": "ru",
    "spanish": "es",
    "swedish": "sv",
    "turkish": "tr",
    "ukrainian": "uk",
    "vietnamese": "vi",
}

# List of supported languages by MyMemoryTranslator
myMemory_lang = {
    "auto detect": "auto",
    "afrikaans": "af",
    "albanian": "sq",
    "amharic": "am",
    "arabic": "ar",
    "armenian": "hy",
    "azerbaijani": "az",
    "basque": "eu",
    "belarusian": "be",
    "bengali": "bn",
    "bosnian": "bs",
    "bulgarian": "bg",
    "burmese": "my",
    "catalan": "ca",
    "cebuano": "ceb",
    "chinese": "zh-CN",
    "chinese traditional": "zh-TW",
    "corsican": "co",
    "czech": "cs",
    "danish": "da",
    "dutch": "nl",
    "english": "en",
    "esperanto": "eo",
    "estonian": "et",
    "filipino": "fil",
    "filipino (tagalog)": "tl",
    "finnish": "fi",
    "french": "fr",
    "galician": "gl",
    "georgian": "ka",
    "german": "de",
    "greek": "el",
    "gujarati": "gu",
    "haitian": "ht",
    "hausa": "ha",
    "hawaiian": "haw",
    "hebrew": "he",
    "hindi": "hi",
    "hungarian": "hu",
    "icelandic": "is",
    "indonesian": "id",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "javanese": "jw",
    "kannada": "kn",
    "kazakh": "kk",
    "khmer": "km",
    "korean": "ko",
    "kurdish": "ku",
    "lao": "lo",
    "latin": "la",
    "latvian": "lv",
    "lithuanian": "lt",
    "luxembourgish": "lb",
    "macedonian": "mk",
    "malay": "ms",
    "malayalam": "ml",
    "maltese": "mt",
    "maori": "mi",
    "marathi": "mr",
    "mongolian": "mn",
    "nepali": "ne",
    "norwegian": "no",
    "persian": "fa",
    "polish": "pl",
    "portuguese": "pt",
    "punjabi": "pa",
    "romanian": "ro",
    "russian": "ru",
    "samoan": "sm",
    "serbian": "sr",
    "spanish": "es",
    "sundanese": "su",
    "swahili": "sw",
    "swedish": "sv",
    "tajik": "tg",
    "tamil": "ta",
    "telugu": "te",
    "thai": "th",
    "turkish": "tr",
    "ukrainian": "uk",
    "urdu": "ur",
    "uzbek": "uz",
    "vietnamese": "vi",
    "welsh": "cy",
    "xhosa": "xh",
    "yiddish": "yi",
    "yoruba": "yo",
}


def verify_language_in_key(lang: str, engine: str) -> bool:
    """Verify if the language is in the key of the engine

    Parameters
    ----------
    lang : str
        Language to verify
    engine : str
        Engine to verify

    Returns
    -------
    bool
        True if the language is in the key of the engine

    Raises
    ------
    ValueError
        If the engine is not found

    """
    if engine == "Google Translate":
        return lang in google_lang.keys()
    elif engine == "LibreTranslate":
        return lang in libre_lang.keys()
    elif engine == "MyMemoryTranslator":
        return lang in myMemory_lang.keys()
    else:
        raise ValueError("Engine not found")


# select target engine
gLang_target = list(google_lang.keys())
gLang_target.pop(0)
gLang_target.sort()

libre_target = list(libre_lang.keys())
libre_target.pop(0)
libre_target.sort()

myMemory_target = list(myMemory_lang.keys())
myMemory_target.pop(0)
myMemory_target.sort()

engine_select_target_dict = {
    "Tiny (~32x speed)": ["English"],
    "Base (~16x speed)": ["English"],
    "Small (~6x speed)": ["English"],
    "Medium (~2x speed)": ["English"],
    "Large (v1) (1x speed)": ["English"],
    "Large (v2) (1x speed)": ["English"],
    "Google Translate": [up_first_case(x) for x in gLang_target],
    "LibreTranslate": [up_first_case(x) for x in libre_target],
    "MyMemoryTranslator": [up_first_case(x) for x in myMemory_target],
}

# source engine
# For source engine we need to check wether the language is compatible with whisper or not
# if not then we remove it from the list
google_whisper_compatible = list(google_lang.keys())
for lang in google_whisper_compatible:
    if lang not in whisper_compatible:
        google_whisper_compatible.remove(lang)

libre_whisper_compatible = list(libre_lang.keys())
for lang in libre_whisper_compatible:
    if lang not in whisper_compatible:
        libre_whisper_compatible.remove(lang)

myMemory_whisper_compatible = list(myMemory_lang.keys())
for lang in myMemory_whisper_compatible:
    if lang not in whisper_compatible:
        myMemory_whisper_compatible.remove(lang)

whisper_compatible_uppercase = [up_first_case(x) for x in whisper_compatible]
whisper_source = ["Auto detect"] + whisper_compatible_uppercase
whisper_source.sort()

google_source = ["Auto detect"] + [up_first_case(x) for x in google_whisper_compatible]
google_source.sort()

libre_source = ["Auto detect"] + [up_first_case(x) for x in libre_whisper_compatible]
libre_source.sort()

myMemory_source = ["Auto detect"] + [up_first_case(x) for x in myMemory_whisper_compatible]
myMemory_source.sort()

engine_select_source_dict = {
    "Tiny (~32x speed)": whisper_source,
    "Base (~16x speed)": whisper_source,
    "Small (~6x speed)": whisper_source,
    "Medium (~2x speed)": whisper_source,
    "Large (v1) (1x speed)": whisper_source,
    "Large (v2) (1x speed)": whisper_source,
    "Google Translate": google_source,
    "LibreTranslate": libre_source,
    "MyMemoryTranslator": myMemory_source,
}
