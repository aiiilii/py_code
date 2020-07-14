from typing import List
import queue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeKSortedLists:

    # using pq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode()
        l3 = dummy
        pq = queue.PriorityQueue() # default is minheap

        for idx, node in enumerate(lists):
            if node:
                pq.put((node.val, idx, node)) # double parens are needed

        while not pq.empty():
            _, idx, node = pq.get()
        
            l3.next = node
            l3 = l3.next
            
            if l3.next:
                pq.put((node.next.val, idx, node.next))

        return dummy.next