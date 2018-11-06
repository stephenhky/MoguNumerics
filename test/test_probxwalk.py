
import mogu.probxwalk as xwalk
import unittest


class test_probxwalk(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_uniformweights(self):
        example_mapping = {'a': 'A',
                           'b': 'B',
                           'ab': ['A', 'B'],
                           'num': [0, 1, 2]}
        crosswalk = xwalk.compute_uniformweighted_xwalk(example_mapping)
        self.assertEqual(len(crosswalk), 4)
        self.assertAlmostEqual(crosswalk['a']['A'], 1.0, delta=0.0001)
        self.assertAlmostEqual(crosswalk['ab']['A'], 0.5, delta=0.0001)
        self.assertAlmostEqual(crosswalk['ab']['B'], 0.5, delta=0.0001)
        self.assertAlmostEqual(crosswalk['b']['B'], 1.0, delta=0.0001)
        self.assertAlmostEqual(crosswalk['num'][0], 1./3., delta=0.0001)
        self.assertAlmostEqual(crosswalk['num'][1], 1. / 3., delta=0.0001)
        self.assertAlmostEqual(crosswalk['num'][2], 1. / 3., delta=0.0001)

    def test_double_xwalk(self):
        xwalk1 = {'a': {'A': 1}, 'b': {'B': 0.3, 'C': 0.7}}
        xwalk2 = {'A': {1: 1}, 'B': {2: 0.5, 3: 0.5}, 'C': {4: 1}}
        crosswalk = xwalk.compute_resultant_xwalk(xwalk1, xwalk2)
        self.assertAlmostEqual(crosswalk['a'][1], 1, delta=0.0001)
        self.assertAlmostEqual(crosswalk['b'][2], 0.15, delta=0.0001)
        self.assertAlmostEqual(crosswalk['b'][3], 0.15, delta=0.0001)
        self.assertAlmostEqual(crosswalk['b'][4], 0.7, delta=0.0001)


if __name__ == '__main__':
    unittest.main()
