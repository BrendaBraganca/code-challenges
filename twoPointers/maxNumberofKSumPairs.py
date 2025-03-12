class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        esq = 0
        dire = len(nums) - 1
        acc = 0
        while esq < dire:
            if(nums[esq] + nums[dire] < k):
                esq +=1
            elif(nums[esq] + nums[dire] > k):
                dire-=1
            else:
                acc+=1
                esq+=1
                dire-=1
        return acc