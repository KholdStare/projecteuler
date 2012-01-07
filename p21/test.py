import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_221(self):
        self.assertEqual(220, sol.main(221))

    def test_10000(self):
        self.assertEqual(31626, sol.main(10000))


if __name__ == '__main__':
    unittest.main()

