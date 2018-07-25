
from itertools import product

import unittest
import numpy as np

import mogu


class test_random(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sample_correlted_gaussian(self):
        mean = np.array([2., -1.5])
        covmat = np.array([[2.3, -1.1], [-1.1, 1.25]])
        nb_samples = 100000

        # sampling
        rndmat = mogu.random.multivariate.multivar_gaussian(mean, covmat, size=nb_samples)

        # calculating statistics
        sampled_mean = np.mean(rndmat, axis=1)
        sampled_cov = np.cov(rndmat)

        # checking
        for i in range(len(mean)):
            self.assertAlmostEqual(sampled_mean[i],
                                   mean[i],
                                   delta=1.96*np.sqrt(covmat[i, i]/nb_samples))

        # ref: https://stats.stackexchange.com/questions/287144/variance-of-a-sample-covariance-for-normal-variables
        corrcoef = covmat[0, 1]/np.sqrt(covmat[0, 0]*covmat[1, 1])
        cov_of_cov = np.array([[2*covmat[0, 0]*covmat[0, 0], (1+corrcoef*corrcoef)*covmat[0, 0]*covmat[1, 1]],
                               [(1+corrcoef*corrcoef)*covmat[0, 0]*covmat[1, 1], 2*covmat[1, 1]*covmat[1, 1]]])
        cov_of_cov /= np.sqrt(nb_samples-1.)
        for i, j in product(range(len(mean)), range(len(mean))):
            self.assertAlmostEqual(sampled_cov[i, j],
                                   covmat[i, j],
                                   delta=1.96*cov_of_cov[i, j])


if __name__ == '__main__':
    unittest.main()