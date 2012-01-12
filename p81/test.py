import sol
import unittest
import os
thisDir = os.path.dirname(os.path.realpath(__file__))

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_small(self):
        self.assertEqual(2427, sol.main(thisDir + "/input_small"))

if __name__ == '__main__':
    unittest.main()

