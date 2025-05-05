class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        i = len(nums)//2
        return nums[i]