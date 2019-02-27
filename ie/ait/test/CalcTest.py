import unittest
from ie.ait.project1.Calc import Calc

class MyTestCase(unittest.TestCase):
    def test_something(self):
        myCalc = Calc()
        myCalc.myPrint()
        myCalc.myPrint()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
