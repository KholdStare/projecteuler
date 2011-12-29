import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(23, sol.main(10))

    def test_2(self):
        self.assertEqual(233168, sol.main(1000))

if __name__ == '__main__':
    unittest.main()

