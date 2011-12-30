import sol
import unittest
import os
thisDir = os.path.dirname(os.path.realpath(__file__))

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(40824, sol.main(thisDir + "/input"))

if __name__ == '__main__':
    unittest.main()

