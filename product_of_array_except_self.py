from typing import List

class ProductExceptSelf:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        res = [0] * length

        res[0] = 1
        for i in range(1, length):
            res[i] = nums[i - 1] * res[i - 1]

        R = 1
        for i in reversed(range(length)):
            res[i] = res[i] * R
            R *= nums[i]

        return res