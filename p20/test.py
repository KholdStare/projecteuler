import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_count_10(self):
        self.assertEqual(27, sol.main(10))

    def test_count_100(self):
        self.assertEqual(648, sol.main(100))


if __name__ == '__main__':
    unittest.main()

