
# must import thisfirst. Ref: # must import this. Ref: https://stackoverflow.com/questions/7932028/setup-py-for-packages-that-depend-on-both-cython-and-f2py?rq=1
from setuptools import setup

import numpy as np
from numpy.distutils.core import setup, Extension

# https://stackoverflow.com/questions/7932028/setup-py-for-packages-that-depend-on-both-cython-and-f2py
# how to include f2py and cython at the same time

try:
    from Cython.Build import cythonize
    dynprog_ext_modules = cythonize([
        'mogu/dynprog/dldist.pyx',
        'mogu/dynprog/lcp.pyx',
        'mogu/spectral/lanczos_tridiagmat.pyx'
    ])
except ImportError:
    dynprog_ext_modules = [
        Extension('mogu.dynprog.dldist', ['mogu/dynprog/dldist.c']),
        Extension('mogu.dynprog.lcp', ['mogu/dynprog/lcp.c']),
        Extension('mogu.spectral.lanczos_tridiagmat', ['mogu/spectral/lanczos_tridiagmat.c'])
    ]


def readme():
    with open('README.md') as f:
        return f.read()


def install_requirements():
    return [package_string.strip() for package_string in open('requirements.txt', 'r')]


setup(name='mogu',
      version="0.8.1",
      description="Collection of Simple Numerical Routines",
      long_description="Collection of simple numerical routines, independent of each other",
      classifiers=[
          "Topic :: Scientific/Engineering :: Information Analysis",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Fortran",
          "Programming Language :: Cython",
          "Programming Language :: C",
          "Topic :: System :: Distributed Computing",
          "License :: OSI Approved :: MIT License",
      ],
      keywords="mogu numerics computation",
      url="https://github.com/stephenhky/MoguNumerics",
      author="Kwan-Yuet Ho",
      author_email="stephenhky@yahoo.com.hk",
      license='MIT',
      packages=['mogu',
                'mogu.fit',
                'mogu.util',
                'mogu.util.derivatives',
                'mogu.assrule',
                'mogu.voterank',
                'mogu.finance',
                'mogu.finance.binomial',
                'mogu.dynprog',
                'mogu.probxwalk',
                'mogu.random',
                'mogu.econ',
                'mogu.tensor',
                'mogu.spectral'],
      package_data={'mogu': ['finance/binomial/*.f90', 'finance/binomial/*.pyf', 'dynprog/*.pyx'],
                    'test': ['*.csv']},
      setup_requires=['numpy', 'Cython'],
      install_requires=install_requirements(),
      tests_require=[
          'unittest2', 'pandas',
      ],
      scripts=['bin/concatenate_dict', 'bin/mogu_minerule', 'bin/price_option'],
      include_dirs=[np.get_include()],
      ext_modules = [Extension( 'binomialtree',
                                sources=['mogu/finance/binomial/binomialtree.f90',
                                         'mogu/finance/binomial/binomialtree.pyf'] ),]
                    +dynprog_ext_modules,
      include_package_data=True,
      test_suite="test",
      zip_safe=False)

