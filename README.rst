Translate
=========
Translate is more or less unified Python API to use translate.google.com and translate.yandex.ru.


Usage
-----
Typical usecase is::

    import translate.yandex
    import translate.google

    translate_en = lambda text: translate.yandex.translate(text, 'en-ru')
    print translate('Coordinate system synchronizes the Dirichlet integral, which implies the desired equality.')

    translate_cn = lambda text: translate.google.translate(text, 'zh-CN', 'ru', 'your-api-key')
    print translate(u'苹果')


Install
-------
Will be available on PyPI.

