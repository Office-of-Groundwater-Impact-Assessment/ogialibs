#!/usr/bin/env python
from setuptools import find_packages, setup
import versioneer


setup(
    name='ogialibs',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/Office-of-Groundwater-Impact-Assessment/ogialibs/',
    description=(
        "Common Python methods for OGIA"
        ),
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['sandbox*', 'tests*']),
    include_package_data=True,
    install_requires=[
        'geopandas>=0.13',
        'pyarrow',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Other/Nonlisted Topic'],
)