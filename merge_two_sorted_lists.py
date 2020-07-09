class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeLists:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode()
        l3 = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        
        l3.next = l1 or l2

        return dummy.next