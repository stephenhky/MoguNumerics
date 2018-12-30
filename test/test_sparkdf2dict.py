
import unittest
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import Row

from mogu.spark import convertRowsToDict

class TestFuzzyLogic(unittest.TestCase):
    def setUp(self):
        # set up Spark context
        conf = SparkConf().setMaster("local[*]")
        conf = conf.setAppName("test_mogu")
        self.sc = SparkContext(conf=conf)
        self.sqlContext = SQLContext(self.sc)

        # set up dataframe
        typicalRow = Row("Name", "Profile")
        typicalProfile = Row("Age", "Gender", "Weight")

        # fake data
        profile1 = typicalProfile(12, "M", 130)
        row1 = typicalRow("Peter", profile1)
        profile2 = typicalProfile(24, "F", 124)
        row2 = typicalRow("Mary", profile2)
        profile3 = typicalProfile(25, "M", 140)
        row3 = typicalRow("John", profile3)
        profile4 = typicalProfile(21, "F", 118)
        row4 = typicalRow("Susan", profile4)

        # dataframe
        self.scdf = self.sqlContext.createDataFrame([row1, row2, row3, row4])

    def tearDown(self):
        pass

    def test_convert2Dict(self):
        jsonobj = convertRowsToDict(self.scdf.collect())
        self.assertEqual(len(jsonobj), 4)
        for obj in jsonobj:
            self.assertEqual(len(obj), 2)
            self.assertTrue('Name' in obj)
            self.assertTrue('Profile' in obj)
            self.assertEqual(type(obj['Profile']), dict)
            self.assertEqual(len(obj['Profile']), 3)


if __name__ == '__main__':
    unittest.main()


