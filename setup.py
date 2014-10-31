#!/usr/bin/env python

import os
import sys

import pygeom

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'pygeom',
]

requires = []

with open('README', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='pygeom',
    version=pygeom.__version__,
    description='a Python package for performing calculations in planar universal geometry',
    long_description=readme + '\n\n' + history,
    author='Tim Leslie',
    author_email='tim.leslie@gmail.com',
    url='https://github.com/timleslie/pygeom',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'pygeom': 'pygeom'},
    include_package_data=True,
    install_requires=requires,
    license='unspecified',
    zip_safe=False,
    classifiers=(
    ),
    extras_require={
    },
)
