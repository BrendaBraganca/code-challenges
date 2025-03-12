class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        ult = len(flowerbed) - 1
        
        while n > 0 and i < len(flowerbed):
            if flowerbed[i] == 0:
                ant = (i == 0 or flowerbed[i - 1] == 0)
                post = (i == ult or flowerbed[i + 1] == 0)

                if ant and post:
                    flowerbed[i] = 1
                    n -= 1
                    i += 1
                
            i += 1 
            
        return n == 0