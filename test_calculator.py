import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(-1,-3),-4)
        self.assertEqual(add(0,100),100)
        self.assertEqual(add(100,101),201)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(100,99),1)
        self.assertEqual(subtract(0,-15),15)
        self.assertEqual(subtract(-10,-10),0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
    #     fill in code
        self.assertEqual(mul(3,4), 12)
        self.assertEqual(mul(-2,5), 10)
        self.assertEqual(mul(0,99), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-9, 3), -3)
        with self.assertRaises(ZeroDivisionError):
            div(10,0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,4),2)
        self.assertEqual(logarithm(3,81),4)
        self.assertEqual(logarithm(5,625),4)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(5,-25)
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-5,2)
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(5,12),13)
        self.assertAlmostEqual(hypotenuse(-6,8),10)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2),2)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()