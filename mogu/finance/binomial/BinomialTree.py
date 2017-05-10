

import numpy as np


class StockBinomialTree:
    '''
    Class that implements the binomial tree with stock price
    '''

    def __init__(self, S0=1.0, r=0.05, sigma=0.05, T=1.0, nbsteps=100):
        '''
        Constructor
        '''
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.nbsteps = nbsteps

        self.initializeParameters()
        self.initializeStockTree()
        self.initializeOptionPriceTree()

    def initializeParameters(self):
        self.dt = self.T / self.nbsteps
        self.rdt = self.r * self.dt
        self.sigma2dt = self.sigma * self.sigma * self.dt
        self.u = np.exp(np.sqrt(self.sigma2dt))
        self.d = 1. / self.u
        self.p = (np.exp(self.rdt)-self.d) / (self.u-self.d)

    def initializeStockTree(self):
        stockTree = []
        for i in range(self.nbsteps + 1):
            js = np.arange(i+1)
            stock = self.S0 * self.u ** (i-js) * self.d ** js
            stockTree.append(stock)
        self.stockTree = stockTree

    def initializeOptionPriceTree(self):
        optionPriceTree = []
        for i in range(self.nbsteps + 1):
            optionPrice = np.zeros(self.nbsteps + 1)
            optionPriceTree.append(optionPrice)
        self.optionPriceTree = optionPriceTree

    def getPrice(self):
        return self.optionPriceTree[0][0]

    def calculateOptionPriceTree(self):
        raise Exception('Not implemented!')


class EuropeanCallBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for European call option
    '''

    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, nbsteps=100):
        '''
        Constructor
        '''
        StockBinomialTree.__init__(self, S0=S0, r=r, sigma=sigma, T=T, nbsteps=nbsteps)
        self.X = X
        self.calculateOptionPriceTree()

    def calculateOptionPriceTree(self):
        for j in range(self.nbsteps + 1):
            self.optionPriceTree[self.nbsteps][j] = max(self.stockTree[self.nbsteps][j] - self.X, 0)
        for i in range(self.nbsteps - 1, -1, -1):
            for j in range(i + 1):
                self.optionPriceTree[i][j] = np.exp(-self.rdt) * (self.p * self.optionPriceTree[i + 1][j] + (1 - self.p) * self.optionPriceTree[i + 1][j + 1])


class EuropeanPutBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for European put option
    '''

    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, nbsteps=100):
        '''
        Constructor
        '''
        StockBinomialTree.__init__(self, S0=S0, r=r, sigma=sigma, T=T, nbsteps=nbsteps)
        self.X = X
        self.calculateOptionPriceTree()

    def calculateOptionPriceTree(self):
        for j in range(self.nbsteps + 1):
            self.optionPriceTree[self.nbsteps][j] = max(self.X - self.stockTree[self.nbsteps][j], 0)
        for i in range(self.nbsteps - 1, -1, -1):
            for j in range(i + 1):
                self.optionPriceTree[i][j] = np.exp(-self.rdt) * (self.p * self.optionPriceTree[i + 1][j] + (1 - self.p) * self.optionPriceTree[i + 1][j + 1])


class AmericanCallBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for American call option
    '''

    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, nbsteps=100):
        '''
        Constructor
        '''
        StockBinomialTree.__init__(self, S0=S0, r=r, sigma=sigma, T=T, nbsteps=nbsteps)
        self.X = X

        self.calculateOptionPriceTree()

    def calculateOptionPriceTree(self):
        for j in range(self.nbsteps + 1):
            self.optionPriceTree[self.nbsteps][j] = max(self.stockTree[self.nbsteps][j] - self.X, 0)
        for i in range(self.nbsteps - 1, -1, -1):
            for j in range(i + 1):
                imValue = self.stockTree[i][j] - self.X
                euroCallValue = np.exp(-self.rdt) * (self.p * self.optionPriceTree[i + 1][j] + (1 - self.p) * self.optionPriceTree[i + 1][j + 1])
                self.optionPriceTree[i][j] = max(imValue, euroCallValue)


class AmericanPutBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for American put option
    '''

    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, nbsteps=100):
        '''
        Constructor
        '''
        StockBinomialTree.__init__(self, S0=S0, r=r, sigma=sigma, T=T, nbsteps=nbsteps)
        self.X = X

        self.calculateOptionPriceTree()

    def calculateOptionPriceTree(self):
        for j in range(self.nbsteps + 1):
            self.optionPriceTree[self.nbsteps][j] = max(self.X - self.stockTree[self.nbsteps][j], 0)
        for i in range(self.nbsteps - 1, -1, -1):
            for j in range(i + 1):
                imValue = self.X - self.stockTree[i][j]
                euroPutValue = np.exp(-self.rdt) * (self.p * self.optionPriceTree[i + 1][j] + (1 - self.p) * self.optionPriceTree[i + 1][j + 1])
                self.optionPriceTree[i][j] = max(imValue, euroPutValue)