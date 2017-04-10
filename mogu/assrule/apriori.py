
from operator import and_
from itertools import combinations
import csv

class AprioriAssociationRule:
    def __init__(self, inputfile):
        self.transactions = []
        self.itemSet = set([])
        inf = open(inputfile, 'rb')
        reader = csv.reader(inf)
        for elements in reader:
            if len(elements)>0:
                self.transactions.append(filter(lambda item: len(item)>0, elements))
                for element in elements:
                    self.itemSet.add(element)
        inf.close()
        self.toRetItems = {}
        self.associationRules = []

    def getSupport(self, itemcomb):
        if type(itemcomb) != frozenset:
            itemcomb = frozenset([itemcomb])
        within_transaction = lambda transaction: reduce(and_, [(item in transaction) for item in itemcomb])
        count = len(filter(within_transaction, self.transactions))
        return float(count)/float(len(self.transactions))

    def runApriori(self, minSupport=0.15, minConfidence=0.6):
        itemCombSupports = filter(lambda freqpair: freqpair[1]>=minSupport,
                                  map(lambda item: (frozenset([item]), self.getSupport(item)), self.itemSet))
        currentLset = set(map(lambda freqpair: freqpair[0], itemCombSupports))
        k = 2
        while len(currentLset)>0:
            currentCset = set([i.union(j) for i in currentLset for j in currentLset if len(i.union(j))==k])
            currentItemCombSupports = filter(lambda freqpair: freqpair[1]>=minSupport,
                                             map(lambda item: (item, self.getSupport(item)), currentCset))
            currentLset = set(map(lambda freqpair: freqpair[0], currentItemCombSupports))
            itemCombSupports.extend(currentItemCombSupports)
            k += 1
        for key, supportVal in itemCombSupports:
            self.toRetItems[key] = supportVal
        self.calculateAssociationRules(minConfidence=minConfidence)

    def calculateAssociationRules(self, minConfidence=0.6):
        for key in self.toRetItems:
            subsets = [frozenset(item) for k in range(1, len(key)) for item in combinations(key, k)]
            for subset in subsets:
                confidence = self.toRetItems[key] / self.toRetItems[subset]
                if confidence > minConfidence:
                    self.associationRules.append([subset, key-subset, confidence])

