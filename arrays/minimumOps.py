class Solution(object):
    def minOperations(self, nums, k):
        nums.sort()
        mini = nums[0]
        if mini < k:
            return -1
        i = 0
        acc = 0
        while(i < len(nums)):
            if(nums[i] > k):
                acc+=1
                while(i + 1 < len(nums) and nums[i] == nums[i +1]):
                    i+=1
            i+=1
        return acc