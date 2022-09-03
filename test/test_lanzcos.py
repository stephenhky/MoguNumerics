
import unittest

import numpy as np

from mogu.spectral import lanzcos


class test_lanzcos(unittest.TestCase):
    def test_four(self):
        tol = 1e-8
        A = np.array(
            [
                [1., 1., 2., -1.],
                [1., 2., -3., 0.],
                [2., -3., -1., 0.],
                [-1., 0., 0., 0.5]
            ]
        )
        eigval1, eigvec1 = np.linalg.eig(A)
        eigval2, eigvec2 = lanzcos(A, A.shape[0])

        assert len(eigval2) == A.shape[0] + 1

        eig1dict = {}
        for i in range(A.shape[0]):
            for j in range(len(eigval2)):
                if abs(eigval1[i] - eigval2[j]) < tol:
                    eig1dict[i] = j
                    break
        assert len(set(eig1dict.values())) == len(eigval1)

        for i in range(A.shape[0]):
            j = eig1dict[i]
            assert np.abs(np.linalg.norm(eigvec2[:, j]) - 1.) < tol
            assert np.all(np.abs(A @ eigvec2[:, j] / eigval2[j] - eigvec2[:, j]) < tol)

    def test_paulix(self):
        tol = 1e-8
        A = np.array(
            [
                [0., 1.],
                [1., 0.]
            ]
        )
        eigval1, eigvec1 = np.linalg.eig(A)
        eigval2, eigvec2 = lanzcos(A, A.shape[0])

        assert len(eigval2) == A.shape[0] + 1

        eig1dict = {}
        for i in range(A.shape[0]):
            for j in range(len(eigval2)):
                if abs(eigval1[i] - eigval2[j]) < tol:
                    eig1dict[i] = j
                    break
        assert len(set(eig1dict.values())) == len(eigval1)

        for i in range(A.shape[0]):
            j = eig1dict[i]
            assert np.abs(np.linalg.norm(eigvec2[:, j]) - 1.) < tol
            assert np.all(np.abs(A @ eigvec2[:, j] / eigval2[j] - eigvec2[:, j]) < tol)
            assert abs(abs(eigvec2[0, j]) - np.sqrt(0.5)) < tol


if __name__ == '__main__':
    unittest.main()
