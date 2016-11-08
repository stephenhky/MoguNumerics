from itertools import product

import numpy as np

# abstract tensor derivatives
def abstract_tensor_derivative_element(tensor_derivative_expression, fcn, X, indices, dx=None, tol=1e-8):
    if dx == None:
        tdx = min(0.1, abs(0.1 * X[indices])) if X[indices] != 0. else 0.1
        df_old = abstract_tensor_derivative_element(tensor_derivative_expression, fcn, X, indices, dx=tdx)
        df_new = abstract_tensor_derivative_element(tensor_derivative_expression, fcn, X, indices, dx=tdx * 0.1)
        while abs(df_new - df_old) > tol:
            df_old = df_new
            tdx *= 0.1
            df_new = abstract_tensor_derivative_element(tensor_derivative_expression, fcn, X, indices, dx=tdx)
        return df_new
    else:
        return tensor_derivative_expression(fcn, X, indices, dx)

def abstract_derivative_gradient(tensor_derivative_expression, fcn, X, *args, **kwargs):
    dfval = np.zeros(X.shape)
    for indices in product(*map(range, X.shape)):
        dfval[indices] = abstract_tensor_derivative_element(tensor_derivative_expression, fcn, X, indices, *args, **kwargs)
    return dfval

def grad_element(fcn, X, indices, dx):
    dX = np.zeros(X.shape)
    dX[indices] = dx
    return (fcn(X + dX) - fcn(X - dX)) / (2 * dx)

def divgrad_element(fcn, X, indices, dx):
    dX = np.zeros(X.shape)
    dX[indices] = dx
    return (fcn(X + dX) - 2 * fcn(X) + fcn(X - dX)) / (dx * dx)

# gradient
def tensor_gradient_element(fcn, X, indices, dx=None, tol=1e-8):
    return abstract_tensor_derivative_element(grad_element, fcn, X, indices, dx=dx, tol=tol)

def tensor_gradient(fcn, X, *args, **kwargs):
    return abstract_derivative_gradient(grad_element, fcn, X, *args, **kwargs)

# divergence of gradient (second derivatives)
def tensor_divgrad_element(fcn, X, indices, dx=None, tol=1e-12):
    return abstract_tensor_derivative_element(divgrad_element, fcn, X, indices, dx=dx, tol=tol)

def tensor_divgrad(fcn, X, *args, **kwargs):
    return abstract_derivative_gradient(divgrad_element, fcn, X, *args, **kwargs)