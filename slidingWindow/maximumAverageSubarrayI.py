class Solution(object):
    def findMaxAverage(self, nums, k):
        maxAverage = 0
        somaJanela = 0

        for i in range(k):
            somaJanela += nums[i]
        
        maxAverage =  somaJanela/float(k)

        for i in range(k, len(nums)):
            somaJanela += nums[i] - nums[i - k]
            maxAverage = max(maxAverage, somaJanela / float(k))
        return maxAverage