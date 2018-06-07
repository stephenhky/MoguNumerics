
import os
import unittest

import numpy as np
import pandas as pd
from mogu.netflow import simvoltage

class test_SocialNetwork(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_socialnetwork(self):
        nodes = ['Stephen', 'John', 'Mary',
                 'Joshua',
                 'Abigail', 'Andrew', 'Jacob', 'Melanie',
                 'Shirley', 'Zoe', 'Wallace', 'Susan',
                 'Urban']
        edges = [('Stephen', 'Jacob', 1),
                 ('Jacob', 'Stephen', 1),
                 ('Stephen', 'Abigail', 1),
                 ('Abigail', 'Stephen', 1),
                 ('Stephen', 'Andrew', 1),
                 ('Andrew', 'Stephen', 1),
                 ('Andrew', 'Abigail', 1),
                 ('Abigail', 'Andrew', 1),
                 ('John', 'Stephen', 1),
                 ('Andrew', 'John', 0.4),
                 ('John', 'Andrew', 0.6),
                 ('Abigail', 'John', 1),
                 ('John', 'Abigail', 1),
                 ('John', 'Mary', 1),
                 ('Mary', 'John', 0.9),
                 ('John', 'Joshua', 1),
                 ('Joshua', 'John', 1),
                 ('John', 'Jacob', 1),
                 ('Jacob', 'John', 1),
                 ('Abigail', 'Jacob', 1),
                 ('Jacob', 'Abigail', 1),
                 ('Jacob', 'Andrew', 1),
                 ('Andrew', 'Jacob', 1),
                 ('Shirley', 'Stephen', 1),
                 ('Stephen', 'Shirley', 1),
                 ('Melanie', 'Stephen', 1),
                 ('Stephen', 'Melanie', 1),
                 ('Melanie', 'Shirley', 1),
                 ('Shirley', 'Urban', 0.2),
                 ('Urban', 'Shirley', 0.21),
                 ('Susan', 'Shirley', 1),
                 ('Shirley', 'Susan', 1),
                 ('Shirley', 'Zoe', 1),
                 ('Zoe', 'Shirley', 1),
                 ('Shirley', 'Wallace', 1),
                 ('Wallace', 'Shirley', 1),
                 ('Zoe', 'Wallace', 1)]
        wn1 = simvoltage.SocialNetworkSimVoltage(nodes=nodes, edges=edges, precalculated_distance=True)

        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        testresults = pd.read_csv(os.path.join(THIS_DIR, 'socialnetworkranks.csv'),
                                  header=None,
                                  names=['name1', 'name2', 'resistance'],
                                  dtype={'name1': str, 'name2': str, 'resistance': np.float})

        for _, row in testresults.iterrows():
            name1 = row['name1']
            name2 = row['name2']
            resistance = row['resistance']
            self.assertAlmostEqual(wn1.getResistance(name1, name2), resistance, places=3)
            print('%s\t%s : %.4f passed.' % (name1, name2, resistance))

    def test_resistdist(self):
        obj = simvoltage.GraphResistanceDistance()
        self.assertAlmostEqual(obj.getResistance('Stephen', 'Sinnie'), 0.6666666666666667, places=4)
        self.assertAlmostEqual(obj.getResistance('Elaine', 'Sinnie'), 0.6666666666666667, places=4)
        self.assertAlmostEqual(obj.getResistance('Elaine', 'Stephen'), 0.6666666666666667, places=4)

if __name__ == '__main__':
    unittest.main()