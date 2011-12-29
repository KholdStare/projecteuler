import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(4613732, sol.main(4e6))

if __name__ == '__main__':
    unittest.main()

