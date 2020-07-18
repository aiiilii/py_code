class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseInK:
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 1:
            return head

        dummy = ListNode()
        dummy.next = head
        begin = dummy # which is prev
        i = 0

        while head:
            i += 1
            if i % k == 0:
                begin = self.reverse(begin, head.next)
                head = begin.next
            else:
                head = head.next

        return dummy.next

    def reverse(self, begin: ListNode, end: ListNode) -> ListNode:
        curr = begin.next
        prev = begin
        first = curr
        curr_next = None

        while curr != end:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        begin.next = prev # prev is the new head after reversing, in the first run, this links dummy to the reversed head
        first.next = curr # curr is at end after reversing, first was the first node but is now the last node after reversing
                        # connect the last node to the end

        return first # first is the last node, thus returning it would be the new prev (begin)