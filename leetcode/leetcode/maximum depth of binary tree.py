class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        l1 = self.maxDepth(root.left)
        l2 = self.maxDepth(root.right)

        return max(l1,l2)+1