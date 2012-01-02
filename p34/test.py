import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_sum(self):
        for n in [1, 2, 145]:
            self.assertEqual(n, sol.sum_of_digits_factorial(n))

#    def test_sol_4(self):
#        self.assertEqual(19316, sol.main(4))
#
#    def test_sol_5(self):
#        self.assertEqual(443839, sol.main(5))


if __name__ == '__main__':
    unittest.main()

