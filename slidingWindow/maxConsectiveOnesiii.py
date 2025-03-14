class Solution(object):
    def longestOnes(self, nums, k):
        start = 0
        maxOnes = 0
        zero_acc = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zero_acc +=1 
        
            while zero_acc > k:
                if nums[start] == 0:
                    zero_acc-=1
                start +=1
            maxOnes =  max(maxOnes, end - start + 1)
        return maxOnes
        
        