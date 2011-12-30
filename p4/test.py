import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_palindrome(self):
        self.assertTrue(sol.is_palindrome(9009))
    
    def test_1(self):
        self.assertEquals(9009, sol.main(2))
    
    def test_1(self):
        self.assertEquals(906609, sol.main(3))

if __name__ == '__main__':
    unittest.main()

