from typing import List

class PermutationsII:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, first=0):
            if first == n:
                res.append(list(nums))
                return

            for i in range(first, n):
                if i > first and nums[i] == nums[first]:
                    continue
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(list(nums), first + 1) # important to pass the value of nums not reference
        
        nums.sort()
        n = len(nums)
        res = []
        backtrack(nums)
        return res