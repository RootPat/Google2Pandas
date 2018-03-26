#!/usr/bin/env python
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
with open(path.join(here, 'LICENSE.txt'), encoding='utf-8') as f:
    license = f.read()

metadata = {\
    'name'              : 'Data2Df',
    'version'           : '0.001',
    'author'            : 'Patrick Harris .',
    'author_email'      : 'sales@panalysis.com',
    'maintainer'        : 'Matt S.',
    'maintainer_email'  : 'sales@panalysis.com',
    'url'               : '',
    'download_url'	: '',
    'description'       : '',
    'long_description'  : ,
    'classifiers'       : ['Development Status :: 4 - Beta', \
                           'Programming Language :: Python', \
                           'Programming Language :: Python :: 2', \
                           'Programming Language :: Python :: 2.7', \
                           'Programming Language :: Python :: 3', \
                           'Programming Language :: Python :: 3.5', \
                           'Intended Audience :: Science/Research', \
                           'Topic :: Scientific/Engineering', \
                           'Operating System :: OS Independent'],
    'license'           : license,
    'install_requires'  : ['numpy>=1.7',
			   'pandas>=0.15',
                           'google-api-python-client',
			   'httplib2'],
    'packages'          : find_packages()}

setup(**metadata)
