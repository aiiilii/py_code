from typing import List

class FourSum:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if not nums or len(nums) < 4:
            return res

        nums.sort()

        for i in range(len(nums) - 3):
            if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                three_sum = target - nums[i]
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or (j > i + 1 and nums[j - 1] != nums[j]):
                        two_sum = three_sum - nums[j]
                        self.twoSum(nums, two_sum, i, j, res)

        return res

    def twoSum(self, nums: List[int], target: int, i: int, j: int, res: List[List[int]]) -> None:
        low = j + 1
        high = len(nums) - 1

        while low < high:
            if nums[low] + nums[high] == target:
                res.append([nums[i], nums[j], nums[low], nums[high]])
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