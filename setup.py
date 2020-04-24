#!/usr/bin/env python3
from setuptools import setup

__author__ = 'Sander Maijers <sander@clarin.eu>'
__version__ = '1.0.dev1'

INSTALL_REQUIRES = ['Mako>1.0,<1.1', 'requests>2.6,<2.8']

setup(
    author=__author__,
    author_email=__author__,
    classifiers=('Natural Language :: English',
                 'Programming Language :: Python', ),
    description='',
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    license='GPLv3',
    name='generate_language_info_pages',
    packages=['generate_language_info_pages'],
    url='https://github.com/clarin-eric/generate_language_info_pages',
    version=__version__,
    zip_safe=False, )
