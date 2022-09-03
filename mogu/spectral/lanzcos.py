
# implementing Lanzco's algorithm

import numpy as np
from scipy.linalg import eigh_tridiagonal


def lanzcos(M, k):
    assert M.shape[0] == M.shape[1]
    assert (M == M.T).all()
    d = M.shape[1]
    assert k <= d

    a = np.zeros(k+1)
    b = np.zeros(k)
    v = np.zeros((d, k+1))

    v[:, 0] = np.random.uniform(size=d)
    v[:, 0] /= np.linalg.norm(v[:, 0])

    a[0] = v[:, 0].T @ M @ v[:, 0]
    v[:, 1] = M @ v[:, 0] - a[0] * v[:, 0]
    v[:, 1] /= np.linalg.norm(v[:, 1])

    for i in range(1, k):
        a[i] = v[:, i].T @ M @ v[:, i]
        b[i-1] = v[:, i-1].T @ M @ v[:, i]
        v[:, i+1] = M @ v[:, i] - a[i] * v[:, i] - b[i-1] * v[:, i-1]
        v[:, i+1] /= np.linalg.norm(v[:, i+1])

    eigvals, eigvecs = eigh_tridiagonal(a, b)
    return eigvals, v @ eigvecs
