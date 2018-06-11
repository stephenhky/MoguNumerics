.. mogu documentation master file, created by
   sphinx-quickstart on Fri Nov 11 17:36:58 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to mogu's documentation!
================================

This is a numerical packages collecting various routines of numerical algorithms.

I tried to make each file to be independent of each other. If there are functions that are universally used,
they will be put into the package `mogu.util`. However, I try my best to keep the number of these functions
as few as possible.

Functionalities
---------------

* Association rule using Apriori algorithm;
* Embedding: Sammon algorithm;
* Binomial tree algorithm for European and American options pricing;
* Exponential and sigmoid curve fitting;
* Simulated voltage for networks;
* Google Page rank;
* Voter rank: Wilson's score;
* Dynamic programming: Damerau-Levenshtein distance;
* Topological data analysis (optimized from [PyTDA](https://github.com/stephenhky/PyTDA)).

Github: Github_

PyPI: PyPI_

To install: type on command prompt: `pip install -U mogu`

Contents:

.. toctree::
   :maxdepth: 2

   news

.. _Github: https://github.com/stephenhky/MoguNumerics
.. _PyPI: https://pypi.org/project/mogu/

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

