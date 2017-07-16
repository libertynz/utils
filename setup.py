# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='utils',
    version='0.1.0',
    description='Handy utilities for python programming',
    long_description=readme,
    author='Brendon Mackenzie',
    author_email='brendon@primitiveman.co.nz',
    url='https://github.com/libertynz/utils',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

