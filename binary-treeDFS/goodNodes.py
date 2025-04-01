class Solution(object):
    def goodNodes(self, root):
        if root is None:
            return 0
        def dfs(root, maxVal):
            if(root is None):
                return
            if(root.val >= maxVal):
                acc[0] = acc[0] + 1
                maxVal = root.val
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        acc = [0]
        dfs(root, root.val)
        return acc[0]