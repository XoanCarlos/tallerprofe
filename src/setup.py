__author__ = "jcarlos"
__date__ = "$Nov 6, 2017 2:48:06 PM$"

from setuptools import setup, find_packages

setup (
       name='TallerProfe',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='jcarlos',
       author_email='',

       summary='Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )