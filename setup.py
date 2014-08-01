#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import events

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = events.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='connector-events',
    version=version,
    description="""Events app primarily for the 'connector' events & community aggregator""",
    long_description=readme + '\n\n' + history,
    author='Ben Lopatin',
    author_email='ben@wellfire.co',
    url='https://github.com/rva-data/connector-events',
    packages=[
        'events',
    ],
    include_package_data=True,
    install_requires=[
        'Markdown>=2.0.0',
        'django-model-utils>=1.0.0',
        'icalendar>=3.5',
        'django-ical>=1.2',
    ],
    license="BSD",
    zip_safe=False,
    keywords='connector-events',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
