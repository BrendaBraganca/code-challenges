class Solution(object):
    def longestZigZag(self, root):
        self.dist = 0
        def dfs(root, andaEsq, cam):
            if root is not None:
                self.dist = max(self.dist, cam)
                if(andaEsq):
                    dfs(root.left, False, cam+1)
                    dfs(root.right, True, 1)
                else:
                    dfs(root.right, True, cam+1)
                    dfs(root.left, False, 1)
        dfs(root, True, 0)
        return self.dist
            
        