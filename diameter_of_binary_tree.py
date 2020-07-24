class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DiameterOfBinaryTree:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.curr_max = 0
        self.max_depth(root)
        return self.curr_max

    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        self.curr_max = max(self.curr_max, left + right)

        return max(left, right) + 1