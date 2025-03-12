class Solution(object):
    def productExceptSelf(self, nums):
        p = 1
        s = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = p
            p *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= s
            s *= nums[i]
        return res