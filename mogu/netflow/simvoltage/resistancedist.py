

'''
Get the resistance distance matrix of a simple undirected network.
See: http://en.wikipedia.org/wiki/Resistance_distance
'''

import numpy as np
from scipy.sparse import dok_matrix

default_nodes = ['Stephen', 'Sinnie', 'Elaine']
default_edges = [('Stephen', 'Sinnie'),
                 ('Elaine', 'Sinnie'),
                 ('Elaine', 'Stephen')]

class GraphResistanceDistance:
    def __init__(self, nodes=default_nodes, edges=default_edges):
        self.initializeClass(nodes, edges)
        self.Omega = self.computeResistanceDistance()
        
    def getResistance(self, node1, node2):
        if self.nodesIdx.has_key(node1) and self.nodesIdx.has_key(node2):
            idx0 = self.nodesIdx[node1]
            idx1 = self.nodesIdx[node2]
            return self.Omega[idx0, idx1]
        else:
            unknown_keys = [node for node in [node1, node2] if not self.nodesIdx.has_key(node)]
            raise Exception('Unknown key(s): '+' '.join(unknown_keys))
    
    def initializeClass(self, nodes, edges):
        self.nodes = nodes
        # all edges are unique
        self.edges = list(set([tuple(sorted(edge)) for edge in edges]))
        self.nodesIdx = {self.nodes[idx]: idx for idx in range(len(self.nodes))}

    def calculateDegreeMatrix(self):
        Dmatrix = dok_matrix((len(self.nodes), len(self.nodes)), dtype=np.float)
        for edge in self.edges:
            for node in edge:
                idx = self.nodesIdx[node]
                Dmatrix[idx, idx] += 1
        return Dmatrix
        
    def calculateAdjacencyMatrix(self):
        Amatrix = dok_matrix((len(self.nodes), len(self.nodes)), dtype=np.float)
        for edge in self.edges:
            idx0 = self.nodesIdx[edge[0]]
            idx1 = self.nodesIdx[edge[1]]
            Amatrix[idx0, idx1] = 1
            Amatrix[idx1, idx0] = 1
        return Amatrix
        
    def computeResistanceDistance(self):
        Dmatrix = self.calculateDegreeMatrix()
        Amatrix = self.calculateAdjacencyMatrix()
        Lmatrix = Dmatrix.toarray() - Amatrix.toarray()
        Lambda = np.linalg.pinv(Lmatrix)
        Omega = dok_matrix((len(self.nodes), len(self.nodes)), dtype=np.float)
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                Omega[i, j] = Lambda[i, i] + Lambda[j, j] - 2 * Lambda[i, j]
        return Omega
