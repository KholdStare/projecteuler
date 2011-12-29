import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(2520, sol.main(10))

    def test_2(self):
        self.assertEqual(232792560, sol.main(20))

if __name__ == '__main__':
    unittest.main()

