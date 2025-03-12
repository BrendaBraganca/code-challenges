class Solution:
    def moveZeroes(self, nums):
        indEsc = 0
        for indLer in range(len(nums)):
            if nums[indLer] != 0:
                nums[indEsc] = nums[indLer]
                indEsc+=1
        for i in range(indEsc, len(nums)):
            nums[i] = 0
        return nums