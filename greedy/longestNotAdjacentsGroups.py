class Solution(object):
    def getLongestSubsequence(self, words, groups):
        res = [words[0]]
        lastGroup = groups[0]
        for i in range(1,len(words)):
            if(groups[i] != lastGroup):
                res.append(words[i])
                lastGroup = groups[i]
        return res