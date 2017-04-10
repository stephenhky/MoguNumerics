import numpy as np
import theano
import theano.tensor as T

from ..util.derivatives import numerical_gradients as ng

# define variables
mf = T.dscalar('mf')         # magic factor / learning rate

# coordinate variables
Xmatrix = T.dmatrix('Xmatrix')
Ymatrix = T.dmatrix('Ymatrix')

# number of points and dimensions (user specify them)
N, d = Xmatrix.shape
_, td = Ymatrix.shape

# grid indices
n_grid = T.mgrid[0:N, 0:N]
ni = n_grid[0].flatten()
nj = n_grid[1].flatten()

# cost function
c_terms, _ = theano.scan(lambda i, j: T.switch(T.lt(i, j),
                                               T.sqrt(T.sum(T.sqr(Xmatrix[i]-Xmatrix[j]))),
                                               0),
                         sequences=[ni, nj])
c = T.sum(c_terms)

s_term, _ = theano.scan(lambda i, j: T.switch(T.lt(i, j),
                                              T.sqr(T.sqrt(T.sum(T.sqr(Xmatrix[i]-Xmatrix[j])))-T.sqrt(T.sum(T.sqr(Ymatrix[i]-Ymatrix[j]))))/T.sqrt(T.sum(T.sqr(Xmatrix[i]-Xmatrix[j]))),
                                              0),
                        sequences=[ni, nj])
s = T.sum(s_term)

E = s / c

# function compilation and optimization
Efcn = theano.function([Xmatrix, Ymatrix], E)

# training
def sammon_embedding(Xmat, initYmat, alpha=0.3, tol=1e-8, maxsteps=500, return_updates=False):
    N, d = Xmat.shape
    NY, td = initYmat.shape
    if N != NY:
        raise ValueError('Number of vectors in Ymat ('+str(NY)+') is not the same as Xmat ('+str(N)+')!')

    # iteration
    Efcn_X = lambda Ymat: Efcn(Xmat, Ymat)
    step = 0
    oldYmat = initYmat
    oldE = Efcn_X(initYmat)
    update_info = {'Ymat': [initYmat], 'cost': [oldE]}
    converged = False
    while (not converged) and step<=maxsteps:
        newYmat = oldYmat - alpha*ng.tensor_gradient(Efcn_X, oldYmat, tol=tol)/ng.tensor_divgrad(Efcn_X, oldYmat, tol=tol)
        newE = Efcn_X(newYmat)
        if np.all(np.abs(newE-oldE)<tol):
            converged = True
        oldYmat = newYmat
        oldE = newE
        step += 1
        if return_updates:
            print 'Step ', step, '\tCost = ', oldE
            update_info['Ymat'].append(oldYmat)
            update_info['cost'].append(oldE)

    # return results
    if return_updates:
        update_info['num_steps'] = step
        return oldYmat, update_info
    else:
        return oldYmat