
import numpy as np

from binomialtree import binomialtree as bt

def compute_bintree_parameters(r, sigma, T, nbsteps):
    dt = T / float(nbsteps)
    rdt = r * dt
    sigma2dt = sigma * sigma * dt
    u = np.exp(np.sqrt(sigma2dt))
    d = 1. / u
    p = (np.exp(rdt) - d) / (u - d)

    return {'dt': dt, 'rdt': rdt, 'sigma2dt': sigma2dt, 'u': u, 'd': d, 'p': p}

def option_pricing(S, X, r, sigma, T, nbsteps, f90func):
    parameters = compute_bintree_parameters(r, sigma, T, nbsteps)
    return f90func(S, X, parameters['rdt'], parameters['p'], parameters['u'], parameters['d'], nbsteps)

def eurocall_price(S, X, r, sigma, T, nbsteps):
    return option_pricing(S, X, r, sigma, T, nbsteps, bt.eurocall)

def europut_price(S, X, r, sigma, T, nbsteps):
    return option_pricing(S, X, r, sigma, T, nbsteps, bt.europut)

def amcall_price(S, X, r, sigma, T, nbsteps):
    return option_pricing(S, X, r, sigma, T, nbsteps, bt.amcall)

def amput_price(S, X, r, sigma, T, nbsteps):
    return option_pricing(S, X, r, sigma, T, nbsteps, bt.amput)
