# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in libyanwing/__init__.py
from libyanwing import __version__ as version

setup(
	name='libyanwing',
	version=version,
	description='new doctype for account dimention',
	author='ARD',
	author_email='Hadeel.milad@ard.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
