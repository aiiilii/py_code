class BasicCalculatorII:

    def calculate(self, s: str) -> int:
        if not str:
            return 0

        num = 0
        stack = []
        pre_sign = '+' # the previous sign

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(s[i])

            if s[i] in "+-*/" or i == len(s) - 1:
                
                if pre_sign == '+':
                    stack.append(num)
                elif pre_sign == '-':
                    stack.append(-num)
                elif pre_sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                pre_sign = s[i]

        return sum(stack)