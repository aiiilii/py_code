class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode()
        l3 = dummy
        carry = 0

        while l1 and l2:
            digit_val = l1.val + l2.val + carry
            l3.next = ListNode(digit_val % 10)
            l3 = l3.next
            carry = int(digit_val / 10)
            l1 = l1.next
            l2 = l2.next

        while l1:
            digit_val = l1.val + carry
            l3.next = ListNode(digit_val % 10)
            l3 = l3.next
            carry = int(digit_val / 10)
            l1 = l1.next

        while l2:
            digit_val = l2.val + carry
            l3.next = ListNode(digit_val % 10)
            l3 = l3.next
            carry = int(digit_val / 10)
            l2 = l2.next

        if carry != 0:
            l3.next = ListNode(carry)

        return dummy.next