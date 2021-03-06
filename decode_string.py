class DecodeString:

    # using 1 stack
    def decodeString(self, s: str) -> str:
        if not str:
            return ""

        stack = []
        curr = ""
        k = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == '[':
                stack.append(k)
                stack.append(curr)
                k = 0
                curr = ""
            elif ch == ']':
                temp = curr
                curr = stack.pop()

                for i in range(stack.pop(), 0, -1):
                    curr += temp
            else:
                curr += ch

        return curr


    # using two stacks
    def decodeString(self, s: str) -> str:
        if not str:
            return ""

        str_stack = []
        int_stack = []
        curr = ""
        k = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == '[':
                int_stack.append(k)
                str_stack.append(curr)
                k = 0
                curr = ""
            elif ch == ']':
                temp = curr
                curr = str_stack.pop()

                for i in range(int_stack.pop(), 0, -1): # decrementing for loop
                    curr += temp
            else:
                curr += ch

        return curr