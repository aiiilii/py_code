from typing import List

class Sums:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums or len(nums) < 3:
            return res

        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)

        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]) -> None:
        low = i + 1
        high = len(nums) - 1
        target = -nums[i]

        while low < high:
            if nums[low] + nums[high] == target:
                res.append([nums[i], nums[low], nums[high]])
                while low < high and nums[low] == nums[low + 1]:
                    low += 1
                while low < high and nums[high] == nums[high - 1]:
                    high -= 1
                low += 1
                high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1