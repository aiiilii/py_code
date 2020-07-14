class AddStrings:
    
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0

        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0

            carry, digit_val = divmod(x1 + x2 + carry, 10)
            res.append(digit_val)
            
            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        # change the list into str by adding each x in casting as str, in reverse order
        return ''.join(str(x) for x in res[::-1]) 