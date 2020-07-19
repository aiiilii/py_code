class Node:
    def __init__(self, x: int, next: 'Node'=None, random: 'Node'=None): # use 'Node' for forward reference
        self.val = int(x)
        self.next = next
        self.random = random

class RandomList:
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        dic = collections.defaultdict(lambda: Node(0)) # set everything to null in the dictionary, placeholder
        dic[None] = None # if operating on an empty list, meaning head == None, then dic[head] == dic[None] == None
        node = head

        while node:
            dic[node].val = node.val
            dic[node].next = dic[node.next] # points to the placeholder in the first run, then when that node is traversed to, then value of the placeholder will change
            dic[node].random = dic[node.random]
            node = node.next
        return dic[head]