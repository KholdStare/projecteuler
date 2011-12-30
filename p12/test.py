import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_5(self):
        self.assertEqual(28, sol.main(5))
    
    def test_50(self):
        self.assertEqual(25200, sol.main(50))

    def test_500(self):
        self.assertEqual(76576500, sol.main(500))


if __name__ == '__main__':
    unittest.main()

