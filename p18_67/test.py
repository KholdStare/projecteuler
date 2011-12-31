import sol
import unittest
import os
thisDir = os.path.dirname(os.path.realpath(__file__))

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_small(self):
        self.assertEqual(23, sol.main(thisDir + "/input_small"))

    def test_18(self):
        self.assertEqual(1074, sol.main(thisDir + "/input_18"))

    def test_67(self):
        self.assertEqual(7273, sol.main(thisDir + "/input_67"))

if __name__ == '__main__':
    unittest.main()

