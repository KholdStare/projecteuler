import seriesutils
import combinatorics
import unittest

class TestCombinatorics(unittest.TestCase):

    def setUp(self):
        pass

# multinomial coefficients ===============================================
    def test_multinomial_1(self):
        self.assertEqual(1, combinatorics.multinomial_coefficient([]))
        self.assertEqual(1, combinatorics.multinomial_coefficient([4]))
    
    def test_multinomial_2(self):
        self.assertEqual(4, combinatorics.multinomial_coefficient([1,3]))
        self.assertEqual(6, combinatorics.multinomial_coefficient([2,2]))

# sterling numbers =======================================================
    def test_sterling_second_0(self):
        self.assertEqual(1, combinatorics.sterling_second(0, 0))

    def test_sterling_second_0_any_n(self):
        self.assertEqual(0, combinatorics.sterling_second(4, 0))

    def test_sterling_second_1(self):
        self.assertEqual(1, combinatorics.sterling_second(1, 1))

    def test_sterling_second_2(self):
        self.assertEqual(1, combinatorics.sterling_second(2, 2))

    def test_sterling_second_4(self):
        self.assertEqual(7, combinatorics.sterling_second(4, 2))

    def test_sterling_second_10(self):
        self.assertEqual(42525, combinatorics.sterling_second(10, 5))

# bell numbers =======================================================
    def test_bell_base(self):
        self.assertEqual(1, combinatorics.bell_number(0))
        self.assertEqual(1, combinatorics.bell_number(1))

    def test_bell_3(self):
        self.assertEqual(5, combinatorics.bell_number(3))
    
    def test_bell_4(self):
        self.assertEqual(15, combinatorics.bell_number(4))

    def test_bell_7(self):
        self.assertEqual(877, combinatorics.bell_number(7))

    def test_bell_14(self):
        self.assertEqual(190899322, combinatorics.bell_number(14))


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

