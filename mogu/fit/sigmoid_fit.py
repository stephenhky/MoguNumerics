import math

import numpy as np

from ..util.derivatives import numerical_gradients as ng


def sigmoid_prob(x, A, B):
    return 1./(1+math.exp(A*x+B))

def label(f, threshold=0.):
    if f == threshold:
        return 0
    else:
        return 1 if f > threshold else -1
        
def entropy_error_fcn(scores, A, B):
    fcnval = 0.
    for score in scores:
        y = label(score)
        t = (y+1) / 2
        p = sigmoid_prob(score, A, B)
        if p > 0 and p < 1:
            fcnval += - t*math.log(p) - (1-t)*math.log(1-p)
        elif p == 0.:
            fcnval += - (1-t)*math.log(1-p)            
        elif p == 1.:
            fcnval += - t*math.log(p)            
    return fcnval
    
def gradient_search_min_entropy_error_fcn(scores, tol=1e-1, sigma=0.1):
    max_score = max(scores)
    min_score = min(scores)
    initA = -30. / (max_score - min_score)
    initB = -0.5*(max_score+min_score) * initA
    
    A = initA
    B = initB
    curr_fcn_val = entropy_error_fcn(scores, A, B)
    converged = False
    while not converged:
        dfA, dfB = ng.tensor_gradient(lambda X: entropy_error_fcn(scores, X[0], X[1]),
                                      np.array([A, B]),
                                      tol=tol)
        new_fcn_val = entropy_error_fcn(scores, A-sigma*dfA, B-sigma*dfB)
        if abs(new_fcn_val-curr_fcn_val) < tol:
            converged=True
        curr_fcn_val = new_fcn_val
        A = A-sigma*dfA
        B = B-sigma*dfB

    return A, B
