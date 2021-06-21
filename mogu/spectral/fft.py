
import numpy as np


def FFT(f):
    nbdata = f.shape[0]
    assert np.log(nbdata) / np.log(2) % 1 == 0.0

    if nbdata == 1:
        return f

    x = FFT(f[0::2])
    y = FFT(f[1::2])

    g = np.zeros(nbdata, dtype=np.complex_)
    for i in range(nbdata // 2):
        w = np.exp(-1j * 2 * np.pi * i / nbdata)
        g[i] = x[i] + w * y[i]
        g[i + nbdata // 2] = x[i] - w * y[i]

    return g


def invFFTrecursive(f):
    nbdata = f.shape[0]
    assert np.log(nbdata) / np.log(2) % 1 == 0.0

    if nbdata == 1:
        return f

    x = invFFTrecursive(f[0::2])
    y = invFFTrecursive(f[1::2])

    g = np.zeros(nbdata, dtype=np.complex_)
    for i in range(nbdata // 2):
        w = np.exp(1j * 2 * np.pi * i / nbdata)
        g[i] = x[i] + w * y[i]
        g[i + nbdata // 2] = x[i] - w * y[i]

    return g


def invFFT(f):
    nbdata = f.shape[0]
    return invFFTrecursive(f) / nbdata

