
import unittest

from mogu.finance.binomial import eurocall_price, europut_price, amcall_price, amput_price

class test_finance(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEuroCall(self):
        self.assertAlmostEquals(eurocall_price(100.0, 110.0, 0.01, 0.01, 10.0, 10000),
                                1.4968152046203613,
                                delta=1e-4)

    def testEuroPut(self):
        self.assertAlmostEquals(europut_price(100.0, 80.0, 0.05, 0.05, 10.0, 10000),
                                5.284386951732304e-06,
                                delta=1e-6)

    def testAmCall(self):
        self.assertAlmostEquals(amcall_price(100.0, 110.0, 0.05, 0.05, 10.0, 10000),
                                33.303010096394594,
                                delta=1e-3)

    def testAmPut(self):
        self.assertAlmostEquals(amput_price(100.0, 80.0, 0.05, 0.05, 10.0, 10000),
                                9.38288088691752e-05,
                                delta=1e-6)


if __name__ == '__main__':
    unittest.main()