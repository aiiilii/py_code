from typing import List

class NextPermutation:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]: # find first decreasing element from the end
            i -= 1

        if i >= 0: # if that first decreasing element is found,
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]: # find the element that is just larger that that element
                j -= 1

            self.swap(nums, i, j) # swap those two elements

        self.reverse(nums, i + 1) # reverse the list after the first found element; 
                                # if the first decreasing element is not found (ex: 4321), then still reverse at 0th index.

    def reverse(self, nums: List[int], start: int) -> None:
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
