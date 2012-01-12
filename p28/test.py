import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_partial_odd_sum(self):
        self.assertEqual(1, sol.partial_sum_odd_squares(0))
        self.assertEqual(10, sol.partial_sum_odd_squares(1))
        self.assertEqual(35, sol.partial_sum_odd_squares(2))

    def test_sol_small(self):
        self.assertEqual(101, sol.main(5))

    def test_sol(self):
        self.assertEqual(669171001, sol.main(1001))

if __name__ == '__main__':
    unittest.main()

