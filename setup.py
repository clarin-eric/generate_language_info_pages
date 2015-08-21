#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

__author__ = 'Sander Maijers <sander@clarin.eu>'
__version__ = '1.0.dev0'

from sys import version_info
from setuptools import setup

required_python_version = (3, 4)

if version_info < required_python_version:
    raise RuntimeError('ERROR: under Python version {0:d}.{1:d}, while version >= {2:d}.{3:d} required. '
                       .format(version_info.major,
                               version_info.minor,
                               required_python_version[0],
                               required_python_version[1]))

install_requires = ['Mako>1.0,<1.1', 'requests>2.6,<2.8']

setup(author=__author__,
      author_email=__author__,
      classifiers=('Natural Language :: English', 'Programming Language :: Python',),
      description='',
      include_package_data=True,
      install_requires=install_requires,
      license='GPLv3',
      name='generate_language_info_pages',
      packages=['generate_language_info_pages'],
      url='https://github.com/clarin-eric/generate_language_info_pages',
      version=__version__,
      zip_safe=False,
)
