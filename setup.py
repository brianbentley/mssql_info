"""Setup script for setuptools installation"""
from setuptools import setup, find_packages


with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='mssql_info',
    version='0.1.0',
    description='Package to Query SQL Browser',
    long_description=README,
    author='Brian Bentley',
    author_email='bbentley@mailworks.org',
    url='https://github.com/brianbentley/mssql_info',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
