class ReverseInteger:

    def reverse(self, x: int) -> int:
        # [1,-1] is an array. When x <0, it means we will pick #1 element of [1,-1], which is '-1'. 
        # Otherwise, when x >0, [x<0] will be false, which is 0. Then, we will pick #0 element of [1,-1], which is '+1'.
        sign = [1, -1][x < 0]
        res = sign * int(str(abs(x))[::-1])
        return res if -(2**31) - 1 < res < 2**31 else 0