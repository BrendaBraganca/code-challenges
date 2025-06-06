class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        n = sorted(set(nums))
        seqs = []
        acc = 1
        for i in range(len(n) - 1):
            if n[i] == n[i + 1] - 1:
                acc += 1
            else:
                seqs.append(acc)
                acc = 1
        seqs.append(acc)
        return max(seqs)