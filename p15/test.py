import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_count_1(self):
        self.assertEqual(2, sol.main(1, 1))

    def test_count_2(self):
        self.assertEqual(6, sol.main(2, 2))

    def test_count_20(self):
        self.assertEqual(137846528820, sol.main(20, 20))

if __name__ == '__main__':
    unittest.main()

