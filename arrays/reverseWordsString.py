class Solution(object):
    def reverseWords(self, s):
        arr = s.split()
        arr.reverse()
        return ' '.join(arr)