class AddBinary:

    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a

        res = ""
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            val1 = val2 = 0
            if i >= 0:
                val1 = int(a[i])
                i -= 1
            if j >= 0:
                val2 = int(b[j])
                j -= 1
            carry, digit = divmod(val1 + val2 + carry, 2)
            res += str(digit)

        return res[::-1]