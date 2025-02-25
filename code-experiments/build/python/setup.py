#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import setuptools
from distutils.core import setup
from distutils.extension import Extension
import numpy as np
try:
    from Cython.Build import cythonize
except:
    def cythonize(x): return m
    
## Use Cython if interface.c is missing.
USE_CYTHON = not os.path.isfile('cython/interface.c') or (
    os.path.getmtime('cython/interface.pyx') > os.path.getmtime('cython/interface.c') + 1)
## Or we force its use on the command line.
if os.getenv('USE_CYTHON') == 'true':
    USE_CYTHON = True

cmdclass = {}
extensions = []

if USE_CYTHON:
    print("NOTE: Using Cython to build interface.")
    # we rename file interface.pyx to _interface.pyx to possibly avoid import error later
    from Cython.Distutils import build_ext
    cmdclass.update({'build_ext': build_ext})
    interface_file = 'cython/interface.pyx'
else:
    print("NOTE: Using precompiled C file to build interface.")
    interface_file = 'cython/interface.c'
    
if True or 'darwin' in sys.platform or 'linux' in sys.platform:
    extensions.append(Extension('cocoex.interface',
                                sources=[interface_file, 'cython/coco.c'],
                                include_dirs=[np.get_include()],
                                ))
if 'linux' in sys.platform:
    extensions.append(Extension('cocoex._interface',
                                sources=[interface_file, 'cython/coco.c'],
                                include_dirs=[np.get_include()],
                                ))

setup(
    name = 'cocoex',
    version = "2.6.2",  # replaced when setup.py.in becomes setup.py
    packages = ['cocoex'],
    package_dir = {'cocoex': 'python'},
    cmdclass=cmdclass,
    # ext_modules = cythonize(extensions),
    ext_modules = extensions,
    url = 'https://github.com/numbbo/coco/',
    license = 'BSD',
    maintainer = ['Dimo Brockhoff', 'Nikolaus Hansen', 'Tea Tusar'],
    maintainer_email = '_-_dimo.brockhoff_-_@_-_inria.fr',
    # author = ['Anne Auger', 'Bernd Bischl', 'Dimo Brockhoff',
    #            'Nikolaus Hansen', 'Olaf Mersmann', 'Petr Posik',
    #            'Mike Preuss',  'Rodolphe le Riche', 'Guenter Rudolph',
    #            'Marc Schoenauer', 'Heike Trautmann'],
    description = 'Benchmarking framework for all types of black-box optimization algorithms.',
    long_description = '...',
    # install_requires = ['numpy>=1.7'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: ??',
        'Intended Audience :: ??',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: ??'
    ]
)
