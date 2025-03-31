class Solution(object):
    def pairSum(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        n = len(nums)
        soma = 0
        for i in range(n//2):
            somaAtual = nums[i] + nums[n - i -1]
            soma = max(soma, somaAtual)
        return soma