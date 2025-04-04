class Solution(object):
    def leafSimilar(self, root1, root2):
        def pegaFolhas(root):
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [root.val]
            return pegaFolhas(root.left) + pegaFolhas(root.right)
        return pegaFolhas(root1) == pegaFolhas(root2)