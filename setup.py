# encoding: utf-8

from setuptools import setup

setup(
    name='translate',
    version='0.1',
    url='https://github.com/sashka/translate',
    license='BSD',
    author='Alexander Saltanov',
    author_email='asd@mokote.com',
    description='More or less unified API to translate.google.com and translate.yandex.ru',
    long_description=open('README.rst', 'r').read(),
    # license='LICENSE.txt',
    packages=['translate'],
    zip_safe=False,
    platforms='any',
    install_requires=['requests'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
