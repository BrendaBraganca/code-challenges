class Solution(object):
    def pathSum(self, root, targetSum):
        def dfs(root, somaAtual):
            if root is None:
                return 0
            somaAtual+=root.val
            acc= somaPrefixAcc[somaAtual - targetSum]
            somaPrefixAcc[somaAtual]+=1


            acc+=dfs(root.left, somaAtual)
            acc+=dfs(root.right, somaAtual)

            somaPrefixAcc[somaAtual]-=1
            return acc
        somaPrefixAcc = defaultdict(int)
        somaPrefixAcc[0] = 1
        return dfs(root, 0)