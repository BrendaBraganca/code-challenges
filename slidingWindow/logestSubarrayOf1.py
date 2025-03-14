class Solution(object):
    def longestSubarray(self, nums):
        start = 0  
        end = 0  
        k = 1  

        while end < len(nums):
            if nums[end] == 0:
                k -= 1
            
            end += 1  

            if k < 0:  
                if nums[start] == 0:
                    k += 1  
                start += 1  

        return end - start - 1  