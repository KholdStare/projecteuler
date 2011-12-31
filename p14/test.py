import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_count_13(self):
        self.assertEqual(10, sol.count_sequence_steps(13, sol.problem_rule))


if __name__ == '__main__':
    unittest.main()

