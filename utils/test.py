import seriesutils
import unittest

class TestSeriesUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_sum_cons_same(self):
        self.assertEqual(0, seriesutils.sum_consecutive_nums(0,0))
        self.assertEqual(10, seriesutils.sum_consecutive_nums(10,10))

    def test_sum_cons_diff(self):
        self.assertEqual(15, seriesutils.sum_consecutive_nums(1,5))
        self.assertEqual(55, seriesutils.sum_consecutive_nums(1,10))

    def test_sum_cons_equivalence(self):
        """Test equivalence of sum_consecutive_nums, to subtracting two
        partial sums."""
        k = 7
        n = 40
        result = seriesutils.sum_consecutive_nums(k,n)
        partial_difference = seriesutils.partial_sum(n) - seriesutils.partial_sum(k-1)

        self.assertEqual(partial_difference, result)

if __name__ == '__main__':
    unittest.main()

