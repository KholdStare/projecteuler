import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_sol(self):
        self.assertEqual(4179871, sol.main())

if __name__ == '__main__':
    unittest.main()

