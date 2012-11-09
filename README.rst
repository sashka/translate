Translate
=========
Translate is more or less unified Python API to use translate.google.com and translate.yandex.ru.


Usage
-----
Typical use case is::

    import translate.yandex
    import translate.google

    translate_en = lambda text: translate.yandex.translate(text, 'en-ru')
    print translate_en('Coordinate system synchronizes the Dirichlet integral, which implies the desired equality.')

    translate_cn = lambda text: translate.google.translate(text, 'zh-CN', 'ru', 'your-api-key')
    print translate_cn(u'苹果')


Advanced
--------
More advanced use case contains so-called "translation chains". 
A chain lets me to have at least one fallback function.  If one translation function has failed, next is called::

    import translate.yandex
    import translate.google
    import translate.utils

    ytranslate_en = lambda text: translate.yandex.translate(text, 'en-ru')
    gtranslate_en = lambda text: translate.google.translate(text, 'en', 'ru', 'your-api-key')

    translate_en = translate.utils.chain(gtranslate, ytranslate)
    print translate_en("Calm down, I'm a doctor!")


If failure is expensive either in terms of time or money, I can use ``marked_chain`` — when function has failed with 
``TranslationError`` it will never be called again::

    translate_en = translate.utils.marked_chain(gtranslate, ytranslate)


Install
-------
Will be available on PyPI.

