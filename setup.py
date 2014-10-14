#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join, dirname
from setuptools import setup, find_packages

setup(
    name='django-rest-interface',
    version='0.0.1',
    packages=find_packages(),
    requires=['python (>= 2.7)'],
    description='Django REST interface',
    long_description=open(join(dirname(__file__), 'README')).read(),
    author='42 Coffee Cups',
    author_email='contact@42cc.co',
    url='https://github.com/42cc/django-rest-interface',
    download_url='https://github.com/42cc/django-rest-interface/archive/master.zip',
    license='BSD License',
    keywords=['django', 'rest'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
