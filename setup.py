#!/usr/bin/env python

from setuptools import setup, find_packages

#one line description
with open('DESCRIPTION') as F:
    description = F.read().strip()

#version number
with open('VERSION') as F:
    version = F.read().strip()

entry_points = {
    'console_scripts': [
        'tui = tui.cli:dispatch'
        ]}

setup(name='tui',
      version=version,
      description=description,
      author='Mark Fiers',
      author_email='mark.fiers.42@gmail.com',
      entry_points = entry_points,
      include_package_data=True,
      url='https://encrypted.google.com/#q=Tui&safe=off',
      packages=find_packages(),
      install_requires=[
                'Leip',
                'sqlalchemy',
                ],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        ]
     )
