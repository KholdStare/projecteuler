import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_12(self):
        self.assertEqual(60, sol.main(12))
    
    def test_1000(self):
        self.assertEqual(31875000, sol.main(1000))


if __name__ == '__main__':
    unittest.main()

