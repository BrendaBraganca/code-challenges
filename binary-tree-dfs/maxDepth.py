class Solution(object):
    def maxDepth(self, root):
        if root is None:  
            return 0
        altEsq = self.maxDepth(root.left) 
        altDir = self.maxDepth(root.right)
        return 1 + max(altEsq, altDir)