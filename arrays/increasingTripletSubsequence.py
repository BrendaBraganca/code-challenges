class Solution(object):
    def increasingTriplet(self, nums):
        prim = float('inf')  
        sec = float('inf') 
        for num in nums:
            if num <= prim:
                prim = num 
            elif num <= sec:
                sec = num  
            else:
                return True
        
        return False