
import networkx as nx


default_nodes = ['Stephen', 'Sinnie', 'Elaine']
default_edges = [('Stephen', 'Sinnie', 0.2),
                 ('Sinnie', 'Stephen', 0.2),
                 ('Sinnie', 'Elaine', 0.3),
                 ('Elaine', 'Sinnie', 0.2),
                 ('Stephen', 'Elaine', 1.1),
                 ('Elaine', 'Stephen', 1.2)]


class SocialNetworkSimVoltage:
    def __init__(self, nodes=default_nodes, edges=default_edges):
        self.initializeClass(nodes, edges)

    def initializeClass(self, nodes, edges):
        self.constructSocialNetwork(nodes, edges)
        self.errTol = 1e-4
        self.maxSteps = 10000

    def constructSocialNetwork(self, nodes, edges):
        self.wordNet = nx.DiGraph()
        self.wordNet.add_nodes_from(nodes)
        self.wordNet.add_weighted_edges_from(edges)
        
    def checkPersonIrrelevant(self, person, person1, person2):
        path1 = nx.algorithms.shortest_path(self.wordNet,
                                            source = person1, target = person,
                                            weight='weight')
        path2 = nx.algorithms.shortest_path(self.wordNet,
                                            source = person, target = person2,
                                            weight='weight')
        intersection_paths = list(set(path1) & set(path2))
        return (len(intersection_paths) != 1)

    def initloop(self, person1, person2):
        volDict = {}
        for node in self.wordNet:
            if node == person1:
                volDict[node] = 1.0
                continue
            elif node == person2:
                volDict[node] = 0.0
                continue
            elif self.checkPersonIrrelevant(node, person1, person2):
                volDict[node] = 10.0
                continue
            distFrom1 = float(nx.shortest_path_length(self.wordNet, person1, node, weight='weight'))
            distFrom2 = float(nx.shortest_path_length(self.wordNet, node, person2, weight='weight'))
            volDict[node] = distFrom2 / (distFrom1 + distFrom2)
        return volDict

    def compute_incurrent(self, node, volDict):
        in_current = 0
        for pred in self.wordNet.predecessors(node):
            if (volDict[pred] > volDict[node]) and (volDict[pred] >= 0.0) and (volDict[pred] <= 1.0):
                potDiff = volDict[pred] - volDict[node]
                resEdge = self.wordNet[pred][node]['weight']
                in_current += potDiff / resEdge
        return in_current

    def compute_outcurrent(self, node, volDict):
        out_current = 0
        for succ in self.wordNet.successors(node):
            if (volDict[node] > volDict[succ]) and (volDict[succ] >= 0.0) and (volDict[succ] <= 1.0):
                potDiff = volDict[node] - volDict[succ]
                resEdge = self.wordNet[node][succ]['weight']
                out_current += potDiff / resEdge
        return out_current

    def average_VR(self, node, volDict):
        sumVOverR = 0.0
        numRecR = 0.0
        for pred in self.wordNet.predecessors(node):
            if (volDict[pred] > volDict[node]) and (volDict[pred] >= 0.0) and (volDict[pred] <= 1.0):
                resEdge = self.wordNet[pred][node]['weight']
                sumVOverR += volDict[pred] / resEdge
                numRecR += 1. / resEdge
        for succ in self.wordNet.successors(node):
            if (volDict[node] > volDict[succ]) and (volDict[succ] >= 0.0) and (volDict[succ] <= 1.0):
                resEdge = self.wordNet[node][succ]['weight']
                sumVOverR += volDict[succ] / resEdge
                numRecR += 1. / resEdge
        return sumVOverR, numRecR

    def getResistance(self, person1, person2, printVol = False):
        if person1 == person2:
            return 0.0
        try:
            distTwoWords = nx.shortest_path_length(self.wordNet, person1, person2, weight='weight')
        except nx.exception.NetworkXNoPath:
            return float('inf')

        # initialization
        volDict = self.initloop(person1, person2)
        if printVol:
            print(volDict)
        tempVolDict = {node: volDict[node] for node in self.wordNet}

        # iteration: computing the potential of each node
        converged = False
        step = 0
        while (not converged) and step < self.maxSteps:
            tempConverged = True
            for node in self.wordNet:
                if node == person1:
                    tempVolDict[node] = 1.0
                    continue
                elif node == person2:
                    tempVolDict[node] = 0.0
                    continue
                elif (volDict[node] < 0.0) or (volDict[node] > 1.0):
                    tempVolDict[node] = 10.0
                    continue
                in_current = self.compute_incurrent(node, volDict)
                out_current = self.compute_outcurrent(node, volDict)
                if abs(in_current - out_current) > self.errTol:
                    sumVOverR, numRecR = self.average_VR(node, volDict)
                    tempVolDict[node] = 0.0 if numRecR==0 else sumVOverR / numRecR
                    tempConverged = False
                else:
                    tempConverged = tempConverged and True
            converged = tempConverged
            # value update
            for node in self.wordNet:
                volDict[node] = tempVolDict[node]
            step += 1
            if printVol:
                print(volDict)

        # calculating the resistance
        startCurrent = sum([(1.0-volDict[rootsucc])/self.wordNet[person1][rootsucc]['weight']
                            for rootsucc in self.wordNet.successors(person1) if volDict[rootsucc]<=1.0])
        return (1.0 / startCurrent)
                                
    def drawNetwork(self):
        nx.draw(self.wordNet)
        

        

