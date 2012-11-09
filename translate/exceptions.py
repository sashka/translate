class TranslationError(Exception):
    pass


class ServiceFailure(TranslationError):
    pass


class TextTooLong(TranslationError):
    pass


class LanguageNotSupported(TranslationError):
    pass


class LanguageNotDetected(TranslationError):
    pass


class TranslationChainFailure(TranslationError):
    pass