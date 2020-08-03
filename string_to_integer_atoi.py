class StringToInteger:

    def myAtoi(self, str: str) -> int:
        if not str:
            return 0

        str = str.strip()
        if not str:
            return 0

        res = 0
        start_idx = 0
        is_neg = False

        if str[0] in '+, -':
            start_idx += 1
            if str[0] == '-':
                is_neg = True

        for i in range(start_idx, len(str)):
            if not str[i].isdigit():
                break
            digit_val = int(str[i])
            res = res * 10 + digit_val

        if is_neg:
            res = -res

        if res > 2**31 - 1:
            res = 2**31 - 1
        if res < -2**31:
            res = -2**31

        return int(res)