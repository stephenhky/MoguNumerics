
# must import thisfirst. Ref: # must import this. Ref: https://stackoverflow.com/questions/7932028/setup-py-for-packages-that-depend-on-both-cython-and-f2py?rq=1
from setuptools import setup

import numpy as np
from numpy.distutils.core import setup, Extension

from Cython.Build import cythonize

# https://stackoverflow.com/questions/7932028/setup-py-for-packages-that-depend-on-both-cython-and-f2py
# how to include f2py and cython at the same time

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='mogu',
      version="0.2.0",
      description="Collection of Simple Numerical Routines",
      long_description="Collection of simple numerical routines, independent of each other",
      classifiers=[
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: MIT License",
      ],
      keywords="mogu numerics computation",
      url="https://github.com/stephenhky/MoguNumerics",
      author="Kwan-Yuet Ho",
      author_email="stephenhky@yahoo.com.hk",
      license='MIT',
      packages=['mogu',
                'mogu.embed',
                'mogu.fit',
                'mogu.util',
                'mogu.util.derivatives',
                'mogu.netflow',
                'mogu.assrule',
                'mogu.voterank',
                'mogu.finance',
                'mogu.finance.binomial',
                'mogu.dynprog',
                'mogu.topology',
                'mogu.probxwalk'],
      package_data={'mogu': ['finance/binomial/*.f90', 'finance/binomial/*.pyf', 'dynprog/*.pyx'],
                    'test': ['*.csv']},
      setup_requires=['numpy', 'Cython'],
      install_requires=[
          'Cython', 'numpy', 'scipy', 'numba', 'tensorflow', 'networkx>=2.0', 'graphflow>=0.1.1', 'mogutda',
      ],
      tests_require=[
          'unittest2', 'pandas',
      ],
      scripts=['bin/concatenate_dict', 'bin/mogu_minerule', 'bin/price_option', 'bin/mogu_sammon'],
      include_dirs=[np.get_include()],
      ext_modules = [Extension( 'binomialtree',
                                sources=['mogu/finance/binomial/binomialtree.f90',
                                         'mogu/finance/binomial/binomialtree.pyf'] ),]
                    +cythonize(['mogu/dynprog/dldist.pyx',
                                'mogu/dynprog/lcp.pyx']),
      include_package_data=True,
      test_suite="test",
      zip_safe=False)

