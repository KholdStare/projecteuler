import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_main(self):
        self.assertEqual(171, sol.main(1901, 2000))


if __name__ == '__main__':
    unittest.main()

