import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_sum(self):
        for n in [1634, 8208, 9474]:
            self.assertEqual(n, sol.sum_of_digits_to_power(n, 4))

    def test_sol_4(self):
        self.assertEqual(19316, sol.main(4))

    def test_sol_5(self):
        self.assertEqual(443839, sol.main(5))


if __name__ == '__main__':
    unittest.main()

