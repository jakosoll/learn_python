import unittest


def factorize(x):
    if x < 0:
        raise ValueError("Value must be positive")
    if not isinstance(x, int):
        raise TypeError("Value must be integer")
    if x == 1:
        return x
    return x * factorize(x - 1)


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        cases = ['string', 1.5]
        for x in cases:
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        cases = [-1, -10, -100]
        for x in cases:
            with self.subTest(x=x):
                self.assertRaises(ValueError, factorize, x)

    def test_simple_numbers(self):
        cases = {5: 120, 4: 24, 10: 3628800}
        for x, y in cases.items():
            with self.subTest(x=x):
                self.assertEqual(factorize(x), y)


if __name__ == "__main__":
    unittest.main()
