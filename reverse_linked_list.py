class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseLinkedList:
    
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        reversed = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed

    
    def reverseList1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev = None
        curr = head
        curr_next = None

        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

        return prev