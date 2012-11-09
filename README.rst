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


More advanced use case contains so-called "translation chains". If one translation function has failed, next is called::

    import translate.yandex
    import translate.google
    import translate.utils

    ytranslate_en = lambda text: translate.yandex.translate(text, 'en-ru')
    gtranslate_en = lambda text: translate.google.translate(text, 'en', 'ru', 'your-api-key')

    # We may call Google and Yandex on every invocation of ``translate_en``.
    translate_chain = translate.utils.chain(gtranslate, ytranslate)
    print translate_chain("Calm down, I'm a doctor!")

    # If Google failed it will never be called again.
    translate_chain2 = translate.utils.marked_chain(gtranslate, ytranslate)
    print translate_chain2("Calm down, I'm a doctor!")


Install
-------
Will be available on PyPI.

