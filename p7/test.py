import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(13, sol.main(6))

    def test_2(self):
        self.assertEqual(104743, sol.main(10001))

if __name__ == '__main__':
    unittest.main()

