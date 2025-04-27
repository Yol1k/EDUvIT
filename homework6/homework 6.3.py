import unittest
import sys
import math

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_numbers_from_1_to_7(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, factorial, -1)

    def test_maxsize_numbers(self):
        self.assertRaises(ValueError, factorial, 100)

    def test_all_available_numbers(self):
        for n in range(1,100):
            if math.factorial(n) > sys.maxsize:
                break
            self.assertEqual(factorial(n), math.factorial(n))

if __name__ == '__main__':
    unittest.main()
