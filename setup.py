from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='mogu',
      version="0.0",
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
      packages=['mogu',],
      install_requires=[
          'numpy', 'scipy', 'theano',
      ],
      include_package_data=True,
      zip_safe=False)