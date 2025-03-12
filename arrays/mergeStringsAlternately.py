class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = 0
        j = 0
        res = []
        while i < len(word1) and j < len(word2):
            if((i + j) % 2 == 0):
                res.append(word1[i])
                i+=1
            else:
                res.append(word2[j])
                j+=1
        while(i < len(word1)):
            res.append(word1[i])
            i+=1
        while(j< len(word2)):
            res.append(word2[j])
            j+=1
        return ''.join(res)