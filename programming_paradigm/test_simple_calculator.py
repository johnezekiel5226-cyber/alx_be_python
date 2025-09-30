import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # Test add method
    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-2, 7), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    # Test subtract method
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    # Test multiply method
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    # Test divide method (normal cases)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)

    # Test divide by zero
    def test_divide_by_zero(self):
        self.assertEqual(self.calc.divide(10, 0), "Cannot divide by zero.")

if __name__ == '__main__':
    unittest.main()
