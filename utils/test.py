import seriesutils
import combinatorics
import bigops
import numutils
import unittest

class TestBigOps(unittest.TestCase):

    def setUp(self):
        pass

# conversion operations ==================================================
    def test_conversion_to_list(self):
        for num in xrange(0, 1000, 13):
            self.assertEqual(num, bigops.list_to_int(bigops.int_to_list(num)))


# multiplication operation ===============================================
    def test_mul_trivial(self):
        self.assertEqual(1, bigops.list_to_int(bigops.mul([1], [1])))
        for num in xrange(0, 1000, 13):
            self.assertEqual(num, bigops.list_to_int(\
                                    bigops.mul(\
                                      bigops.int_to_list(num), [1] ) ) )

    def test_mul_simple(self):
        a = 123
        b = 456
        self.assertEqual(a*b, bigops.list_to_int(bigops.mul(bigops.int_to_list(a), \
                                                            bigops.int_to_list(b))))

    def test_mul_sequence_trivial(self):
        self.assertEqual(1, bigops.list_to_int(bigops.mul_sequence([])))
        for num in xrange(0, 1000, 13):
            self.assertEqual(num, bigops.list_to_int(\
                                    bigops.mul_sequence(\
                                      [bigops.int_to_list(num)] ) ) )

    def test_mul_sequence_factorial(self):
        n = 10
        self.assertEqual(combinatorics.factorial(n), \
                         bigops.list_to_int(\
                            bigops.mul_sequence(( bigops.int_to_list(d) for d in xrange(1, n+1) )) ) )

# summation operation ====================================================
    def test_sum_sequence_trivial(self):
        self.assertEqual(0, bigops.list_to_int(bigops.sum_sequence([])))
        for num in xrange(0, 1000, 13):
            self.assertEqual(num, bigops.list_to_int(\
                                    bigops.sum_sequence(\
                                      [bigops.int_to_list(num)] ) ) )

    def test_sum_sequence_triangle(self):
        n = 100 # 100th triangle number
        self.assertEqual(seriesutils.partial_sum(n),
                         bigops.list_to_int(\
                                    bigops.sum_sequence(\
                                       ( bigops.int_to_list(x) for x in xrange(1, n+1) ) ) ) )
                                    
    def test_sum_sequence_resolve_carries(self):
        """An interesting side effect of the implementation, is that carries can be stored
        in the digit cells as numbers bigger than 10, and propagated afterwards."""
        result = 56088
        convolution = [ 4, 13, 28, 27, 18 ]
        self.assertEqual(result,
                         bigops.list_to_int(\
                            bigops.sum_sequence(\
                                [ convolution, [0] ] ) ) )
    
    def test_resolve_carries(self):
        """An interesting side effect of the implementation, is that carries can be stored
        in the digit cells as numbers bigger than 10, and propagated afterwards."""
        result = 56088
        convolution = [ 4, 13, 28, 27, 18 ]
        bigops.resolve_carries(convolution)
        self.assertEqual(result, bigops.list_to_int(convolution) )

    def test_add_no_carries(self):
        """Tests if addition with no carries works correctly."""
        terms = [        [ 6, 12, 18 ], \
                     [ 5, 10, 15,  0 ], \
                 [ 4,  8, 12,  0,  0 ] ]
        result = [ 4, 13, 28, 27, 18 ]

        acc = bigops.add_no_carry(terms[0], terms[1])
        acc = bigops.add_no_carry(acc, terms[2])

        for t in zip(result, acc):
            self.assertEqual(t[0], t[1])

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

class TestNumUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_sum_prop_divisors(self):
        self.assertEqual(284, numutils.sum_proper_divisors(220))

    def test_sum_prop_divisors(self):
        self.assertTrue(numutils.is_amicable(220))

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

