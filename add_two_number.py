class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        carry = 0
        dummy = l3 = ListNode()
        
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, val = divmod(val1 + val2 + carry, 10)
            l3.next = ListNode(val)
            l3 = l3.next
            
        return dummy.next



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