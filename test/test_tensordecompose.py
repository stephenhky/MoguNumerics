
import unittest
import numpy as np
import numpy.testing as npt
from itertools import product

from mogu.tensor import decompose_tensor_jennrich


class test_tensordecomposition(unittest.TestCase):
    def test_jennrich(self):
        # definining a rank-3 tensor
        x1 = np.array([[-1.3, 1], [2, -1.4]], dtype=np.float32)
        x2 = np.array([[1, 0], [-1.5, 0.6]], dtype=np.float32)
        x = np.zeros((2, 2, 2))
        x[:, :, 0] = x1
        x[:, :, 1] = x2

        # Jennrich decomposition
        eigvecs_u, eigvecs_v, eigvecs_w = decompose_tensor_jennrich(x)

        # verification
        xh = np.zeros(x.shape)
        for i, j, k in product(range(x.shape[0]), range(x.shape[1]), range(x.shape[2])):
            xh[i, j, k] = sum([eigvecs_u[i, alpha] * eigvecs_v[j, alpha] * eigvecs_w[k, alpha] for alpha in
                               range(eigvecs_u.shape[1])])

        # asserting
        npt.assert_almost_equal(x, xh, decimal=4)


if __name__ == '__main__':
    unittest.main()