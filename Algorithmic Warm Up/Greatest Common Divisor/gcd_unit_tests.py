import unittest
from gcd import gcd, gcd_naive


class TestGCD(unittest.TestCase):
    def test_small(self):
        for (a, b) in [(1, 1), (2, 6), (5, 4)]:
            self.assertEqual(gcd(a, b), gcd_naive(a, b))

    def test_large(self):
        for (a, b, d) in [(28851538, 1183019, 17657) ]:
            self.assertEqual(gcd(a, b), d)

    def test_2(self):
        self.assertEqual(1, gcd(18, 35))

if __name__ == '__main__':
    unittest.main()
