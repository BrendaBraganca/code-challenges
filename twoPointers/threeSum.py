def threeSum(self, nums):
    nums.sort()
    tam = len(nums)
    res = []

    for i in range(tam-2):
        if i > 0 and nums[i] == nums[i -1]:
            continue
        esq = i +1
        dire = tam -1

        while esq < dire:
            soma = nums[i] + nums[esq] + nums[dire]

            if soma == 0:
                res.append([nums[i], nums[esq], nums[dire]])

                while esq < dire and nums[esq] == nums[esq + 1]:
                    esq += 1
                while esq < dire and nums[dire] == nums[dire - 1]:
                    dire -= 1

            if soma > 0:
                esq +=1
            else:
                dire-=1
    return res

        