
import numpy as np
import numba as nb


@nb.njit(nb.complex64[:](nb.complex64[:]))
def slowDFT(t):
    N = t.shape[0]
    omega = np.zeros(N, dtype=np.complex_)
    for n in range(N):
        omega[n] = sum(t[m] * np.exp(-1j*2*np.pi*m*n/N) for m in range(N))
    return omega


@nb.njit(nb.complex64[:](nb.complex64[:]))
def slowInvDFT(omega):
    N = omega.shape[0]
    t = np.zeros(N, dtype=np.complex_)
    for m in range(N):
        t[m] = sum(omega[n] * np.exp(1j*2*np.pi*m*n/N) for n in range(N)) / N
    return t
