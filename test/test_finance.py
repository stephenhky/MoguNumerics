
import unittest

from mogu.finance.binomial import eurocall_price

class test_finance(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEuroCall(self):
        self.assertAlmostEquals(eurocall_price(100, 110, 0.01, 0.01, 10, 10000),
                                1.4968152046203613,
                                delta=1e-4)

if __name__ == '__main__':
    unittest.main()