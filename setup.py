import os
import sys
from codecs import open

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

assert sys.version_info[0] == 3, "steepdata requires Python > 3"


def readme_file():
    return 'README.rst' if os.path.exists('README.rst') else 'README.md'


def license_file():
    return 'LICENSE' if os.path.exists('LICENSE') else 'LICENSE.txt'


setup(
    name='steepdata',
    version='0.0.3',
    description='Python Utilities for parsing STEEM blockchain',
    long_description=open(readme_file()).read(),
    url='https://github.com/Chainers/steepdata',
    author='@steepshot',
    author_email='steepshot.org@gmail.com',
    license=open(license_file()).read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='steem steemit steepdata',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'steep-steem',
        'pymongo',
        'funcy',
        'werkzeug',
        'toolz'
    ],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
