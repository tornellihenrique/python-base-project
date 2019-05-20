# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='base python application',
    version='1.0.0',
    description='Organização básica de projeto python',
    long_description=readme,
    author='Henrique Tornelli Duarte',
    url='https://github.com/henriquetornelli/python-base-project',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'src'))
)

