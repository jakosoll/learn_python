import unittest


class IsPalindromeTest(unittest.TestCase):
    def test_palindrome(self):
        case = [1001, 202, 45454, 50000005]
        for x in case:
            with self.subTest(x=x):
                self.assertTrue(is_palindrome(x), 'False')

    def test_not_palindrome(self):
        self.assertIsNotNone(is_palindrome(1010))
        self.assertFalse(is_palindrome(1011))


def is_palindrome(num):
    mod = num
    new = 0
    while mod > 0:
        new = (new * 10) + (mod % 10)
        mod //= 10
    return new == num


if __name__ == '__main__':
    unittest.main()
