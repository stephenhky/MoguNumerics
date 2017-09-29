import numpy as np
#import networkx as nx

from f90pagerank import f90pagerank as fpr

def GoogleMatrix(digraph, beta):
    nodedict = {node: idx for idx, node in zip(range(len(digraph)), digraph.nodes())}
    A = np.matrix((1 - beta) / float(len(digraph)) * np.ones(shape=(len(digraph), len(digraph))))
    for node1, node2 in digraph.edges():
        A[nodedict[node2], nodedict[node1]] += beta / float(len(list(digraph.successors(node1))))
    return A, nodedict


def L1norm(r1, r2):
    return np.sum(abs(r1 - r2))


def CalculatePageRank(digraph, beta, eps=1e-4, maxstep=1000, fortran=False):
    A, nodes = GoogleMatrix(digraph, beta)

    if fortran:
        r = fpr.compute_pagerank(A, eps, maxstep)
        nodepr = {node: r[nodes[node]] for node in nodes}
    else:
        r = np.transpose(np.matrix(np.repeat(1 / float(len(digraph)), len(digraph))))
        converged = False
        stepid = 0
        while not converged and stepid < maxstep:
            newr = A * r
            converged = (L1norm(newr, r) < eps)
            r = newr
            stepid += 1
        nodepr = {node: r[nodes[node],0] for node in nodes}
    return nodepr
