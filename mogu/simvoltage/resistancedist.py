

'''
Get the resistance distance matrix of a simple undirected network.
See: http://en.wikipedia.org/wiki/Resistance_distance
'''

import numpy as np

class GraphResistanceDistance:
    def __init__(self, nodes=None, edges=None):
        if nodes==None or edges==None:
            nodes = ['Stephen', 'Sinnie', 'Elaine']
            edges = [('Stephen', 'Sinnie'),
                     ('Elaine', 'Sinnie'),
                     ('Elaine', 'Stephen')]
        self.initializeClass(nodes, edges)
        self.Omega = self.computeResistanceDistance()
        
    def getResistance(self, node1, node2):
        if self.nodesIdx.has_key(node1) and self.nodesIdx.has_key(node2):
            idx0 = self.nodesIdx[node1]
            idx1 = self.nodesIdx[node2]
            return self.Omega[idx0, idx1]
        else:
            return None
    
    def initializeClass(self, nodes, edges):
        self.nodes = nodes
        # all edges are unique
        edges_set = set([])
        for edge in edges:
            edges_set.add(tuple(sorted(edge)))
        self.edges = list(edges_set) 
        
        self.nodesIdx = {}
        for idx in range(len(self.nodes)):
            self.nodesIdx[self.nodes[idx]] = idx
            
    def calculateDegreeMatrix(self):
        Dmatrix = np.zeros([len(self.nodes), len(self.nodes)])
        for edge in self.edges:
            for node in edge:
                idx = self.nodesIdx[node]
                Dmatrix[idx, idx] += 1
        return Dmatrix
        
    def calculateAdjacencyMatrix(self):
        Amatrix = np.zeros([len(self.nodes), len(self.nodes)])
        for edge in self.edges:
            idx0 = self.nodesIdx[edge[0]]
            idx1 = self.nodesIdx[edge[1]]
            Amatrix[idx0, idx1] = 1
            Amatrix[idx1, idx0] = 1
        return Amatrix
        
    def computeResistanceDistance(self):
        Dmatrix = self.calculateDegreeMatrix()
        Amatrix = self.calculateAdjacencyMatrix()
        Lmatrix = Dmatrix - Amatrix
        Lambda = np.linalg.pinv(Lmatrix)
        Omega = np.zeros([len(self.nodes), len(self.nodes)])
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                Omega[i, j] = Lambda[i, i] + Lambda[j, j] - 2 * Lambda[i, j]
        return Omega
