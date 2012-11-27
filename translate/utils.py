# encoding: utf-8

from translate.exceptions import TranslationError, TranslationChainFailure


def chain(*funcs):
    """
    Simple translation chain.
    If one function failed, try with another one.
    When all of them failed, TranslationChainFailure exception is raised.
    """
    def translate(text):
        for f in funcs:
            try:
                rv = f(text)
                if rv:
                    return rv
            except TranslationError:
                continue
        raise TranslationChainFailure()
    return translate


def marked_chain(*funcs):
    """
    Marked translation chain.
    If one function failed, try with another one.
    If a function failed once it will never be called again.
    When all functions are failed, TranslationChainFailure exception is raised.
    """
    dead = set()

    def translate(text):
        for f in funcs:
            if f in dead:
                continue
            try:
                rv = f(text)
                if rv:
                    return rv
            except TranslationError:
                dead.add(f)
        raise TranslationChainFailure()

    return translate
