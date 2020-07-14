from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    h = {}
    for i, num in enumerate(nums): # i is the index, num is the element in nums
        n = target - num
        if n not in h:
            h[num] = i
        else: # n is already in h, then find the index of n in h
            return [h[n], i]