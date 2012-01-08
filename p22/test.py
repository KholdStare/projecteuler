import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_alpha_val(self):
        self.assertEqual(53, sol.alphabetical_value("COLIN"))


if __name__ == '__main__':
    unittest.main()

