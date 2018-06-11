
import unittest

import mogu

class TestFuzzyLogic(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_similarity(self):
        self.assertEqual(mogu.dynprog.damerau_levenshtein('debug', 'deubg'), 1)
        self.assertEqual(mogu.dynprog.longest_common_prefix('debug', 'debuag'), 4)


if __name__ == '__main__':
    unittest.main()
