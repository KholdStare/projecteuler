import sol
import unittest
import os
thisDir = os.path.dirname(os.path.realpath(__file__))

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_large(self):
        self.assertEqual("5537376230390876637302048746832985971773659831892672", sol.main(thisDir + "/input"))

if __name__ == '__main__':
    unittest.main()

