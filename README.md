# Mogu: a Collection of Simple Numerical Routines

[![CircleCI](https://circleci.com/gh/stephenhky/MoguNumerics.svg?style=svg)](https://circleci.com/gh/stephenhky/MoguNumerics.svg)
[![GitHub release](https://img.shields.io/github/release/stephenhky/MoguNumerics.svg?maxAge=3600)](https://github.com/stephenhky/MoguNumerics/releases)
[![Updates](https://pyup.io/repos/github/stephenhky/MoguNumerics/shield.svg)](https://pyup.io/repos/github/stephenhky/MoguNumerics/)
[![Python 3](https://pyup.io/repos/github/stephenhky/MoguNumerics/python-3-shield.svg)](https://pyup.io/repos/github/stephenhky/MoguNumerics/)


This is a numerical packages collecting various routines of numerical algorithms. This is not only for convenience, but also demonstration.

I tried to make each file to be independent of each other. If there are functions that are universally used, they will be put into the package `mogu.util`. However, I try my best to keep the number of these functions as few as possible.

# Installation

You must have `numpy` pre-installed. GCC and GFORTRAN compilers have to be available in the machine.
After ensuring they have been installed, type the following to install `mogu`:

```
>>> pip install -U mogu
```


# Functionalities

* Association rule using apriori algorithm;
* Binomial tree algorithm for European and American options pricing;
* Exponential and sigmoid curve fitting;
* Simulated voltage for networks; (moved to new package [graphflow](https://github.com/stephenhky/GraphFlow) since release 0.1.12)
* Google Page rank; (moved to new package [graphflow](https://github.com/stephenhky/GraphFlow) since release 0.1.12)
* Voter rank: Wilson's score;
* Dynamic programming: Damerau-Levenshtein distance;
* Topological data analysis; (implementation moved to [`moguTDA`](https://github.com/stephenhky/MoguTDA) since release 0.1.13)
* Gini coefficients;
* Multivariate Gaussian distribution sampling;
* Probability crosswalk;
* Tensor decomposition using Jennrich algorithm and alternating lease square (ALS) method;
* Discrete Fourier transform (DFT);
* Fast Fourier transform (FFT).

# News

* 06/21/2021: `mogu` 0.7.0 released.
* 01/16/2020: `mogu` 0.6.0 released.
* 09/07/2019: `mogu` 0.5.1 released.
* 08/26/2019: `mogu` 0.5.0 released.
* 01/07/2019: `mogu` 0.4.1 released.
* 12/30/2018: `mogu` 0.4.0 released.
* 11/06/2018: `mogu` 0.3.0 released.
* 07/25/2018: `mogu` 0.2.1 released.
* 06/18/2018: `mogu` 0.2.0 released.
* 06/12/2018: `mogu` 0.1.13 released.
* 04/12/2018: `mogu` 0.1.12 released.
* 03/10/2018: `mogu` 0.1.11 released.
* 03/09/2018: `mogu` 0.1.10 released.
* 03/02/2018: `mogu` 0.1.9 released.
* 02/22/2018: `mogu` 0.1.8 released.
* 12/08/2017: `mogu` 0.1.7 released.
* 09/29/2017: `mogu` 0.1.6 released.
* 08/10/2017: `mogu` 0.1.5 released.
* 06/01/2017: `mogu` 0.1.4 released.
* 05/25/2017: `mogu` 0.1.3 released.
* 05/10/2017: `mogu` 0.1.2 released.
* 04/10/2017: `mogu` 0.1.1 released.
* 04/05/2017: `mogu` 0.1.0 released.
* 11/08/2016: `mogu` 0.0 released.
