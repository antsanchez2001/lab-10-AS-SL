#https://github.com/antsanchez2001/lab-10-AS-SL
#Partner 1: Anthony Sanchez
#Partner 2: Seungmin Lee

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self): # 3 assertions
        self.asserEqual(multiply(3,3),9)
        self.assertNotEqual(multiply(3,2),9)
        self.assertEqual(multiply(0,3),0)
        self.assertEqual(multiply(-1,2),-2)

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,2),1)
        self.assertNotEqual(div(2,2),4)
        self.assertEqual(div(2,-1),-0.5)

 ##########################

    def test_subtract(self):
        self.assertEqual(sub(5, 2), 3)
        self.assertEqual(sub(2, 5), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)


    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)  # base can't be 1

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(-1, 10)
        with self.assertRaises(ValueError):
            log(2, -10)
        with self.assertRaises(ValueError):
            log(0, 100)
    def test_hypotenuse(self): # 3 assertions
        assert math.isclose(math.hypot(3, 4), 5.0)
        assert math.isclose(math.hypot(5, 12), 13.0)
        assert math.isclose(math.hypot(0, 0), 0.0)
    def test_sqrt(self): # 3 assertions
        assert math.isclose(square_root(25), 5.0)

        assert math.isclose(square_root(0), 0.0)
        assert math.isclose(square_root(16),4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()