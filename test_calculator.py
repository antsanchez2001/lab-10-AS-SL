import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.asserEqual(multiply(3,3),9)
        self.assertNotEqual(multiply(3,2),9)
        self.assertEqual(multiply(0,3),0)
        self.assertEqual(multiply(-1,2),-2)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2,2),1)
        self.assertNotEqual(divide(2,2),4)
        self.assertEqual(divide(2,-1),-0.5)

 ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)  # base can't be 1

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