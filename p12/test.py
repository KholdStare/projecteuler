import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_count_54(self):
        self.assertEqual(8, sol.count_divisors(54, None))

    def test_count_huge(self):
        self.assertEqual(576, sol.count_divisors(76576500, None))

    def test_5(self):
        self.assertEqual(28, sol.main(5))
    
    def test_50(self):
        self.assertEqual(25200, sol.main(50))

    def test_500(self):
        self.assertEqual(76576500, sol.main(500))


if __name__ == '__main__':
    unittest.main()

