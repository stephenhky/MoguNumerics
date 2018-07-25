
import numpy as np

def multivar_gaussian(mean, covariance, size=None):
    # getting shapes
    n = mean.shape[0]
    covmat_shape = covariance.shape

    # number of sampled data
    size = size if not (size is None) else 1

    # checking shape compliance
    assert len(covmat_shape) == 2
    assert covmat_shape[0] == n
    assert covmat_shape[1] == n
    assert np.allclose(covariance, covariance.T, atol=1e-4)

    # diagonalizing covariance matrix
    diagvar, eigvecs = np.linalg.eig(covariance)
    transmat = np.linalg.inv(eigvecs)

    # sampling
    rndmatrix = np.random.normal(size=size*n).reshape((n, size))
    # scale by diagonal variance
    rndmatrix *= np.array([np.sqrt(diagvar)]).T
    # linear transform
    rndmatrix = np.matmul(transmat.T, rndmatrix)
    # adding the mean
    rndmatrix += np.array([mean]).T

    return rndmatrix



# rndmat = multivar_gaussian(np.array([0, 1]), np.array([[1.1, 0.5], [0.5, 1.5]]), size=10000)
# np.mean(rndmat, axis=1)
# np.cov(rndmat)
