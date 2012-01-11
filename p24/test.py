import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_sol(self):
        self.assertEqual("2783915460", sol.main(9, 1e6))

if __name__ == '__main__':
    unittest.main()

