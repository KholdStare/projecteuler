import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.denoms = [1, 2, 5, 10, 20, 50, 100, 200]
        self.solver = sol.Solver(self.denoms, 200)

    def test_sol_1(self):
        self.assertEqual(1, self.solver.getCombinations(1))

    def test_sol_2(self):
        self.assertEqual(2, self.solver.getCombinations(2))

    def test_sol_3(self):
        self.assertEqual(2, self.solver.getCombinations(3))

    def test_sol_4(self):
        self.assertEqual(3, self.solver.getCombinations(4))

    def test_sol(self):
        self.assertEqual(73682, self.solver.getCombinations(200))


if __name__ == '__main__':
    unittest.main()

