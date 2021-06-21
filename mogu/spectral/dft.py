
import numpy as np


def slowDFT(t):
    N = t.shape[0]
    omega = np.zeros(N, dtype=np.complex_)
    for n in range(N):
        omega[n] = np.sum(t[m] * np.exp(-1j*2*np.pi*m*n/N) for m in range(N))
    return omega


def slowInvDFT(omega):
    N = omega.shape[0]
    t = np.zeros(N, dtype=np.complex_)
    for m in range(N):
        t[m] = np.sum(omega[n] * np.exp(1j*2*np.pi*m*n/N) for n in range(N)) / N
    return t
