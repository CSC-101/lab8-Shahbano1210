import group
import unittest

class TestCases(unittest.TestCase):
    # Part 1
    def test_groups_of_3_1(self):
        nums = [1,2,3,4,5,6,7,8,9]
        result = group.groups_of_3(nums)
        expected = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(expected,result)

    def test_groups_of_3_2(self):
        nums = [1,2,3,4,5,6,7,8]
        result = group.groups_of_3(nums)
        expected = [[1,2,3],[4,5,6],[7,8]]
        self.assertEqual(expected,result)
