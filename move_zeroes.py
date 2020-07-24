from typing import List

class MoveZeroes:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        i = -1
        j = 0

        while j < len(nums):
            if nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1