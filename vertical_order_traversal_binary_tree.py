from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class VertivalTraversal:
    
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def bfs(root):
            queue = collections.deque([(root, 0, 0)])
            while queue:
                node, row, col = queue.popleft()
                if node:
                    node_list.append((col, row, node.val))
                    queue.append((node.left, row + 1, col - 1))
                    queue.append((node.right, row + 1, col + 1))

        bfs(root)

        # sort the node_list according to col
        node_list.sort()

        res = collections.OrderedDict()

        for col, row, val in node_list:
            if col in res:
                res[col].append(val)
            else:
                res[col] = [val]
        
        return res.values()