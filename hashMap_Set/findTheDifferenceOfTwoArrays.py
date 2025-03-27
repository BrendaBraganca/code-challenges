class Solution(object):
    def findDifference(self, nums1, nums2):
        cNums1 = set(nums1)
        cNums2 = set(nums2)
        lst1 = list(cNums1 - cNums2)
        lst2 = list(cNums2 - cNums1)
        return [lst1, lst2]