import sol
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        pass

    def test_conversion_342(self):
        self.assertEqual("three hundred and forty two", sol.int_to_english(342))

    def test_conversion_115(self):
        self.assertEqual("one hundred and fifteen", sol.int_to_english(115))

    def test_main(self):
        self.assertEqual(21124, sol.main(1000))


if __name__ == '__main__':
    unittest.main()

