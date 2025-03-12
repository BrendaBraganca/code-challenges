class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""
        
        len_mdc = mdc(len(str1), len(str2))
        return str1[:len_mdc]