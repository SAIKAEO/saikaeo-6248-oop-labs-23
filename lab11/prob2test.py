import unittest
from prob2code import fib, factorial

class TestFibonacciFactorial(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 362880)

unittest.main()
