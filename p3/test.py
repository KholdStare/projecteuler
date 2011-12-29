import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(29, sol.main(13195))

    def test_1(self):
        self.assertEqual(70, sol.main(600851475143))

if __name__ == '__main__':
    unittest.main()

