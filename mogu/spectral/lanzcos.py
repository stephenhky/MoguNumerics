
# implementing Lanzco's algorithm

import numpy as np


def lanzcos(M, k):
    assert M.shape[0] == M.shape[1]
    assert (M == M.T).all()
    d = M.shape[1]
    assert k <= d

    a = np.zeros(k+1)
    b = np.zeros(k)

    v0 = np.random.uniform(size=d)
    v0 /= np.linalg.norm(v0)

    a[0] = v0.T @ M @ v0
    v1 = M @ v0 - a[0]*v0
    v1 /= np.linalg.norm(v1)

    for i in range(1, k+1):
        a[i] = v1.T @ M @ v1
        b[i-1] = v0.T @ M @ v1
        v2 = M @ v1 - a[i]*v1 - b[i-1]*v0
        v2 /= np.linalg.norm(v2)

        v0, v1 = v1, v2
