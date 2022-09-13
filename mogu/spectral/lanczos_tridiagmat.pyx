
import numpy as np
cimport numpy as np


def prepare_tridiag_vec(np.ndarray M, int k):
    cdef int d = M.shape[1]

    cdef np.ndarray a = np.zeros(k+1)
    cdef np.ndarray b = np.zeros(k)
    cdef np.ndarray v = np.zeros((d, k+1))

    v[:, 0] = np.random.uniform(size=d)
    v[:, 0] = v[:, 0] / np.linalg.norm(v[:, 0])

    a[0] = v[:, 0].T @ M @ v[:, 0]
    v[:, 1] = M @ v[:, 0] - a[0] * v[:, 0]
    v[:, 1] = v[:, 1] / np.linalg.norm(v[:, 1])

    for i in range(1, k):
        a[i] = v[:, i].T @ M @ v[:, i]
        b[i-1] = v[:, i-1].T @ M @ v[:, i]
        v[:, i+1] = M @ v[:, i] - a[i] * v[:, i] - b[i-1] * v[:, i-1]
        v[:, i+1] = v[:, i+1] / np.linalg.norm(v[:, i+1])

    return a, b, v
