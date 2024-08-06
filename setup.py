#!/usr/bin/env python
from setuptools import setup


setup(
    name='ogialibs',
    version='0.1.1',
    description=(
        "Common Python methods for OGIA"
        ),
    long_description='README.md',
    packages=["ogialibs",],
    install_requires=[
        'geopandas>=0.13',
        'pyarrow',
    ],
)
