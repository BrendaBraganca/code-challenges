import math

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        tam = len(nums)
        closest = float('inf')
        somaMaisProx = 0 

        for i in range(tam - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            esq = i + 1
            dire = tam - 1

            while esq < dire:
                soma = nums[i] + nums[esq] + nums[dire]
                dist = abs(target - soma)

                if dist < closest:
                    closest = dist
                    somaMaisProx = soma

                
                if soma < target:
                    esq += 1
                else:
                    dire -= 1

        return somaMaisProx