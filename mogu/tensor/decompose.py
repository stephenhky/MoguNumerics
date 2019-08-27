
import numpy as np
from itertools import product


def decompose_tensor_jennrich(rank3tensor):
    # initialize two random variables
    a = np.random.uniform(size=rank3tensor.shape[2])
    b = np.random.uniform(size=rank3tensor.shape[2])

    # T_a and T_b
    Ta = sum(rank3tensor[:, :, i ] *a[i] for i in range(rank3tensor.shape[2]))
    Tb = sum(rank3tensor[:, :, i ] *b[i] for i in range(rank3tensor.shape[2]))

    # eigenvalues of various auxilliary matrices
    eigvals_u, eigvecs_u = np.linalg.eig(np.matmul(Ta, np.linalg.pinv(Tb)))
    eigvals_v, eigvecs_v = np.linalg.eig(np.transpose(np.matmul(np.linalg.pinv(Ta), Tb)))

    # pair up reciprocal eigenvalues
    # pair up eigenvalues of Ta and Tb
    idx_pairs = []
    tol = 1e-5

    for i, eigval_u in enumerate(eigvals_u):
        for j, eigval_v in enumerate(eigvals_v):
            if abs(eigval_u - 1/ eigval_v) < tol:
                idx_pairs += [(i, j)]
                break

    # solving for third eigenvectors
    nbcomp = len(idx_pairs)
    solved = False
    while not solved:
        try:
            A = np.zeros((nbcomp * rank3tensor.shape[2], nbcomp * rank3tensor.shape[2]))
            B = np.zeros(nbcomp * rank3tensor.shape[2])
            eqidx = 0
            ij_combs = list(tuple(product(range(rank3tensor.shape[0]), range(rank3tensor.shape[1]))))
            for k in range(rank3tensor.shape[2]):
                for ij_comb_idx in np.random.choice(range(len(ij_combs)), size=nbcomp, replace=False):
                    i, j = ij_combs[ij_comb_idx]
                    B[eqidx] = rank3tensor[i, j, k]
                    for ck in range(nbcomp):
                        A[eqidx, ck * rank3tensor.shape[2] + k] = eigvecs_u[i, idx_pairs[ck][0]] * eigvecs_v[j, idx_pairs[ck][1]]
                    eqidx += 1

            sol = np.linalg.solve(A, B)
            solved = True   # exception is not caught at this point
        except np.linalg.LinAlgError:
            solved = False
    eigvecs_w = sol.reshape((nbcomp, rank3tensor.shape[2]), order='F')

    # rearranging eigenvectors
    rearranged_eigvecs_u = np.zeros(shape=eigvecs_u.shape)
    rearranged_eigvecs_v = np.zeros(shape=eigvecs_v.shape)
    for i, (u_idx, v_idx) in enumerate(idx_pairs):
        rearranged_eigvecs_u[:, i] = eigvecs_u[:, u_idx]
        rearranged_eigvecs_v[:, i] = eigvecs_v[:, v_idx]
    rearranged_eigvecs_w = eigvecs_w

    # return values
    return rearranged_eigvecs_u, rearranged_eigvecs_v, rearranged_eigvecs_w
