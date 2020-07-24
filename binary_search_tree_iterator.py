import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    
    def __init__(self, root: TreeNode):
        self.q = collections.deque([])
        self.inorder(root)

    def inorder(self, root: TreeNode) -> None:
        if not root:
            return
        self.inorder(root.left)
        self.q.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            return self.q.popleft()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.q) > 0