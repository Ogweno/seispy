#!/usr/bin/env python
from setuptools import find_packages, setup
packages=find_packages()

VERSION = "1.1"
setup(name='seispy',
      version=VERSION,
      author='Mijian Xu',
      author_email='gomijianxu@gmail.com',
      license='GNU',
      packages=find_packages(),
      package_dir={'seispy': 'seispy'},
      install_requires=['obspy'],
      include_package_data=True,
      zip_safe=False
      )
