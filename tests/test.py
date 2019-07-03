import unittest

from blu.utils import get_sequence

class TestMain(unittest.TestCase):

    def test_get_sequence(self):
        a = [1, 2, 3, 4, 3, 2, 1]
        b = [1, 2, 3, 5]
        c = [3, 4, 3]
        d = [3, 2, 1]
        self.assertEqual(get_sequence(0, 0, a, b)[0], [1, 2, 3])
        self.assertEqual(get_sequence(2, 0, a, c)[0], c)
        self.assertEqual(get_sequence(4, 0, a, d)[0], d)

if __name__ == "__main__":
    unittest.main()
