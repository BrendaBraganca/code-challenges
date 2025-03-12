class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelsInS = []
        vowelsInd = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowelsInS.append(s[i])
                vowelsInd.append(i)
        vowelsInS.reverse()
        for i in range(len(vowelsInd)):
            s[vowelsInd[i]] = vowelsInS[i]
        return ''.join(s) 