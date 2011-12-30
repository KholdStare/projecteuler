import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(17, sol.main(10))

    def test_1(self):
        self.assertEqual(142913828922, sol.main(2e6))


if __name__ == '__main__':
    unittest.main()

