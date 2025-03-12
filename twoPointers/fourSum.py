def fourSum(self, nums, target):
    nums.sort()  
    tam = len(nums)
    res = []

    for i in range(tam - 3):  
        if i > 0 and nums[i] == nums[i - 1]:  
            continue

        for j in range(i + 1, tam - 2):  
            if j > i + 1 and nums[j] == nums[j - 1]: 
                continue

            esq = j +1 
            dire = tam - 1  

            while esq < dire:
                soma = nums[i] + nums[j] + nums[esq] + nums[dire]

                if soma == target:
                    res.append([nums[i], nums[j], nums[esq], nums[dire]])

                    
                    while esq < dire and nums[esq] == nums[esq + 1]:
                        esq += 1
                    while esq < dire and nums[dire] == nums[dire - 1]:
                        dire -= 1

                    
                    esq += 1
                    dire -= 1

                elif soma < target:
                    esq += 1  
                else:
                    dire -= 1 

    return res