# encoding: utf-8

"""
Library for Google Translate API.
More details at https://developers.google.com/translate/v2/using_rest
"""

import requests
from translate.exceptions import ServiceFailure, TextTooLong


FORMATS = ('text', 'html')


def languages(key):
    """Returns a list of supported languages."""
    url = 'https://www.googleapis.com/language/translate/v2/languages'
    params = {'key': key}
    r = requests.get(url, params=params)
    return [i['language'] for i in r.json['data']['languages']]


def detect(text, key, format='text'):
    """Detects the language of a text string. Returns """
    if format not in FORMATS:
        raise TypeError('The format should be "plain" or "html"')
    url = 'https://www.googleapis.com/language/translate/v2/detect'
    params = {'q': text, 'key': key}
    r = requests.get(url, params=params)
    return r.json['data']['detections'][0][0]['language']


def translate_many(text, source_lang, target_lang, key, format='text'):
    """Translate text."""
    if format not in FORMATS:
        raise TypeError("The format should be one of %s, not '%s'" % (FORMATS, format))
    url = 'https://www.googleapis.com/language/translate/v2'
    params = {'source': source_lang, 'target': target_lang, 'q': text, 'format': format, 'key': key}
    r = requests.get(url, params=params)
    if not r.ok:
        code = r.status_code
        if code == 414:
            raise TextTooLong()
        else:
            raise ServiceFailure(code)
    return [i['translatedText'] for i in r.json['data']['translations']]


def translate_one(text, source_lang, target_lang, key, format='text'):
    """Translates a given single string."""
    if not isinstance(text, basestring):
        raise TypeError('Text should be a string, not a %s' % type(text).__name__)
    return translate_many(text, source_lang, target_lang, key, format)[0]


# Default translation method.
translate = translate_one
