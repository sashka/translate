# encoding: utf-8

"""
Library for Yandex Translate API.
More details at http://api.yandex.ru/translate/
"""

import requests
from translate.exceptions import TranslationError, ServiceFailure, TextTooLong, LanguageNotDetected, LanguageNotSupported


FORMATS = ('plain', 'html')


def languages():
    """Returns a list of supported languages."""
    r = requests.get('http://translate.yandex.net/api/v1/tr.json/getLangs')
    return r.json['dirs']


def detect(text, format='plain'):
    """
    Detects the language of a text string.
    Throws LanguageNotDetected in case of empty response from Yandex.
    """
    if format not in FORMATS:
        raise TypeError('The format should be one of %s' % (FORMATS,))
    params = {'text': text, 'format': format}
    r = requests.get('http://translate.yandex.net/api/v1/tr.json/detect', params=params)
    code = r.json['code']
    if  code == 200:
        lang = r.json['lang']
        if lang:
            return lang
        raise LanguageNotDetected
    else:
        raise TranslationError(code)


def translate_many(text, lang, format='plain'):
    """
    Translates a given text. Text may be either a string or a list of strings.
    Returns a list of translated strings.
    """
    if format not in FORMATS:
        raise TypeError("The format should be one of %s, not '%s'" % (FORMATS, format))

    params = {'lang': lang, 'text': text, 'format': format}
    r = requests.get('http://translate.yandex.net/api/v1/tr.json/translate', params=params)
    if not r.ok:
        raise ServiceFailure(r.status_code)
    code = r.json['code']
    if code == 200:
        return r.json['text']
    elif code == 413:
        raise TextTooLong
    elif code == 501:
        raise LanguageNotSupported(lang)
    else:
        raise TranslationError(code)


def translate_one(text, lang, format='plain'):
    """Translates a given single string."""
    if not isinstance(text, basestring):
        raise TypeError('Text should be a string, not a %s' % type(text).__name__)
    return translate_many(text, lang, format)[0]


# Default translation method.
translate = translate_one
