class Solution(object):
    def groupAnagrams(self, strs):
        anag = {}
        for w in strs:
            sw = ''.join(sorted(w))
            if sw not in anag:
                anag[sw]= []
            anag[sw].append(w)
        return list(anag.values())