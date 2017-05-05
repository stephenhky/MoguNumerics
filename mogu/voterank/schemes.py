import numpy as np
from scipy.stats import norm

def diffscore(npos, nneg):
    return npos-nneg

def fracscore(npos, nneg):
    return npos/np.array(npos+nneg, dtype=float)

def wilsonscore(npos, nneg, alpha=0.1):
    num = npos+nneg
    p = fracscore(npos, nneg)
    z = norm.ppf(1.-0.5*alpha)
    denominator = 1+z*z/num
    numerator = p+0.5*z*z/num-z*np.sqrt((p*(1-p)+0.25*z*z/num)/num)
    return numerator/denominator