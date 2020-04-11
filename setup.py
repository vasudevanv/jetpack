"""
jetpack

Collection of commonly used utility functions in python for scientific simulation code.
"""

import os
import jetpack
import setuptools


here = os.path.abspath(os.path.dirname(__file__))


# Package requirements
def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


reqs = parse_requirements(os.path.join(here,'requirements.txt'))


setuptools.setup(
    name='jetpack',
    
    version=jetpack.__version__,
    
    author='Vasu Venkateshwaran',
    author_email='vasu.chemical@gmail.com',
    
    # Project description
    description='Commonly used utility functions in python for scientific simulation code',

    # Source code URL
    url='https://github.com/vasudevanv/jetpack.git',
    
    license='The MIT License',

    classifiers = [
        
        'Development Status :: 2 - Pre-Alpha', 

        'Intended Audience :: Science/Research', 
        'Intended Audience :: Developers',

        'License :: The MIT License',

        'Programming Language :: Python :: 2.7',

        'Topic :: Scientific/Engineering :: Information Analysis',
        
        'Operating System :: POSIX :: Linux',
    ],

    
    packages=setuptools.find_packages(),
    package_data = {'jetpack': ['data/*'], }, 

    # Run-time dependencies
    install_requires=reqs,

    # pytest integration
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

)