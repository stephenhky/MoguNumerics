
import unittest

import numpy as np

from mogu.spectral import slowDFT, slowInvDFT, FFT, invFFT

class test_finance(unittest.TestCase):
    def test_dft(self):
        x = np.array([0, -1.5, -3., -1.5, 0, 1.5, 3., 1.5, 0.])
        k = slowDFT(x)
        inv_x = slowInvDFT(k)
        np.testing.assert_array_almost_equal(x, np.real(inv_x))

    def test_fft(self):
        x = np.array([.25, .75, .75, .25, -.25, -.75, -.75, -.25])
        k = FFT(x)
        inv_x = invFFT(k)
        np.testing.assert_array_almost_equal(x, np.real(inv_x))


if __name__ == '__main__':
    unittest.main()
