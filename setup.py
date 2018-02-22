# from setuptools import setup

from numpy.distutils.core import setup, Extension

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='mogu',
      version="0.1.8",
      description="Collection of Simple Numerical Routines",
      long_description="Collection of simple numerical routines, independent of each other",
      classifiers=[
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Programming Language :: Python :: 2.7",
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
                'mogu.netflow.simvoltage',
                'mogu.netflow.pagerank',
                'mogu.assrule',
                'mogu.voterank',
                'mogu.finance',
                'mogu.finance.binomial',
                'mogu.dynprog',
                'mogu.topology'],
      package_data={'mogu': ['finance/binomial/*.f90', 'finance/binomial/*.pyf',
                             'dynprog/*.c', 'dynprog/*.i', 'dynprog/*.h',
                             'netflow/pagerank/*.f90', 'netflow/pagerank/*.pyf']},
      setup_requires=['numpy',],
      install_requires=[
          'numpy', 'scipy', 'numba', 'tensorflow', 'networkx>=2.0',
      ],
      tests_require=[
          'unittest2',
      ],
      scripts=['bin/concatenate_dict', 'bin/mogu_minerule', 'bin/price_option', 'bin/mogu_sammon'],
      ext_modules = [Extension( 'binomialtree', sources=['mogu/finance/binomial/binomialtree.f90',
                                                         'mogu/finance/binomial/binomialtree.pyf'] ),
                     Extension( 'f90pagerank', sources=['mogu/netflow/pagerank/f90pagerank.f90',
                                                        'mogu/netflow/pagerank/f90pagerank.pyf']),
                     Extension( '_dldist', sources=['mogu/dynprog/dldist_wrap.c',
                                                    'mogu/dynprog/dldist.c']),
                     ],
      # include_package_data=True,
      # test_suite="test",
      zip_safe=False)

