import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(2640, sol.main(10))

    def test_2(self):
        self.assertEqual(25164150, sol.main(100))

if __name__ == '__main__':
    unittest.main()

