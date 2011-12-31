import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_count_13(self):
        self.assertEqual(10, sol.count_sequence_steps(13, sol.problem_rule))

    def test_count_1(self):
        self.assertEqual(1, sol.count_sequence_steps(1, sol.problem_rule))

    def test_20(self):
        self.assertEqual(18, sol.main(20))

    def test_200(self):
        self.assertEqual(171, sol.main(200))

    def test_20000(self):
        self.assertEqual(17647, sol.main(20000))

    def test_2e6(self):
        self.assertEqual(1723519, sol.main(2e6))

    def test_1e6(self):
        self.assertEqual(837799, sol.main(1e6))

if __name__ == '__main__':
    unittest.main()

