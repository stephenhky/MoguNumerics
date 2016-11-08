# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:40:31 2013

@author: hok1
"""

import math

def derivative(fcn, x, dx=None, tol=1e-8):
    if dx == None:
        tdx = min(0.1, abs(0.1 * x)) if x != 0. else 0.1
        df_old = derivative(fcn, x, dx=tdx)
        df_new = derivative(fcn, x, dx=tdx * 0.1)
        while abs(df_old - df_new) > tol:
            df_old = df_new
            tdx *= 0.1
            df_new = derivative(fcn, x, dx=tdx)
        return df_new
    else:
        return (fcn(x + dx) - fcn(x - dx)) / (2 * dx)


def gradient2d(fcn, x, y, tol=1e-7):
    dfx = derivative(lambda xp: fcn(xp, y), x, tol=tol)
    dfy = derivative(lambda yp: fcn(x, yp), y, tol=tol)
    return dfx, dfy

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
        dfA, dfB = gradient2d(lambda A, B: entropy_error_fcn(scores, A, B),
                              A, B, tol=tol)
        new_fcn_val = entropy_error_fcn(scores, A-sigma*dfA, B-sigma*dfB)
        if abs(new_fcn_val-curr_fcn_val) < tol:
            converged=True
        curr_fcn_val = new_fcn_val
        A = A-sigma*dfA
        B = B-sigma*dfB
        #print A, B, curr_fcn_val
    return A, B
