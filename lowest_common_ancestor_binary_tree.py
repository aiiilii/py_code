import collections

class TreeNode:
    def __init__(self, x=0, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class LowestCommonAncestor:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == root:
            return p
        if q == root:
            return q

        queue = collections.deque([root])
        parent_map = {root: None}

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                parent_map[node.left] = node
            if node.right:
                queue.append(node.right)
                parent_map[node.right] = node

        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent_map[p]

        while q not in ancestors:
            q = parent_map[q]

        return q