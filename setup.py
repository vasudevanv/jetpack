import os
import jetpack

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='jetpack',
    
    version=jetpack.__version__,
    
    author='Vasu Venkateshwaran',
    author_email='vasu.chemical@gmail.com',
    
    url='https://github.com/vasudevanv/jetpack.git',
    
    requires=['numpy', 'scipy', 'matplotlib', 'pyyaml'],
    
    license='The MIT License'
)