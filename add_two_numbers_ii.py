class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbersII:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        l3 = None
        carry = 0
        
        while stack1 or stack2 or carry:
            val1 = val2 = 0
            if stack1:
                val1 = stack1.pop()
            if stack2:
                val2 = stack2.pop()

            carry, val = divmod(val1 + val2 + carry, 10)
            new_node = ListNode(val) # reverse direction
            new_node.next = l3
            l3 = new_node

        return l3