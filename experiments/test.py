import unittest
import dynamic

class TestDynamic(unittest.TestCase):

    def setUp(self):
        pass

#################
#  Overlapping  #
#################

    def test_interval_overlap(self):
        a = dynamic.Interval(3, 10)
        b = dynamic.Interval(7, 15)
        self.assertTrue(a.isOverlapping(b))
        self.assertTrue(b.isOverlapping(a))
        b.end = 9
        self.assertTrue(a.isOverlapping(b))
        self.assertTrue(b.isOverlapping(a))

###################################################
#  Solution validity (non overlapping intervals)  #
###################################################

    def test_is_valid_list_empty(self):
        intervalList = [ ]
        self.assertTrue(dynamic.isValidList(intervalList))
    
    def test_is_valid_list_1(self):
        intervalList = [ dynamic.Interval(0, 3, 2) ]
        self.assertTrue(dynamic.isValidList(intervalList))

    def test_is_valid_list_2_overlapping(self):
        intervalList = [ dynamic.Interval(0, 3, 2),
                dynamic.Interval(1, 5, 4) ]
        self.assertFalse(dynamic.isValidList(intervalList))

    def test_is_valid_list_3_sequential(self):
        intervalList = [ dynamic.Interval(0, 3),
                dynamic.Interval(3, 6),
                dynamic.Interval(6, 9) ]
        self.assertTrue(dynamic.isValidList(intervalList))

    def test_is_valid_list_3_overlapping(self):
        intervalList = [ dynamic.Interval(0, 3),
                dynamic.Interval(2, 7),
                dynamic.Interval(6, 9) ]
        self.assertFalse(dynamic.isValidList(intervalList))

####################################
#  Find first compatible interval  #
####################################

    def test_compatible_index_empty(self):
        intervalList = [ ]
        self.assertEquals(dynamic.firstCompatibleIndex(intervalList, 0), -1)

    def test_compatible_index_1(self):
        intervalList = [ dynamic.Interval(0, 3) ]
        self.assertEquals(dynamic.firstCompatibleIndex(intervalList, 0), -1)

    def test_compatible_index_2(self):
        intervalList = [ dynamic.Interval(0, 3),
                dynamic.Interval(2, 5) ]
        self.assertEquals(dynamic.firstCompatibleIndex(intervalList, 0), -1)

    def test_compatible_index_2_success(self):
        intervalList = [ dynamic.Interval(0, 3),
                dynamic.Interval(4, 6) ]
        self.assertEquals(dynamic.firstCompatibleIndex(intervalList, 1), 0)

    def test_compatible_index_many_success(self):
        intervalList = [ dynamic.Interval(0, 3, 2),
                         dynamic.Interval(1, 5, 4),
                         dynamic.Interval(4, 6, 4),
                         dynamic.Interval(2, 9, 7),
                         dynamic.Interval(7, 10, 2),
                         dynamic.Interval(8, 11, 1) ]
        self.assertEquals(dynamic.firstCompatibleIndex(intervalList, 5), 2)

##############
#  Solution  #
##############

    def test_solution(self):
        intervalList = [ dynamic.Interval(0, 3, 2),
                         dynamic.Interval(1, 5, 4),
                         dynamic.Interval(4, 6, 4),
                         dynamic.Interval(2, 9, 7),
                         dynamic.Interval(7, 10, 2),
                         dynamic.Interval(8, 11, 1) ]
        problem = dynamic.WeightedSchedulingProblem(intervalList)
        solutionList = problem.getOptimumList()
        self.assertEquals(solutionList[0], intervalList[0])
        self.assertEquals(solutionList[1], intervalList[2])
        self.assertEquals(solutionList[2], intervalList[4])


if __name__ == '__main__':
    unittest.main()
