import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_count_15(self):
        self.assertEqual(26, sol.main(15))

    def test_count_1000(self):
        self.assertEqual(1366, sol.main(1000))


if __name__ == '__main__':
    unittest.main()

