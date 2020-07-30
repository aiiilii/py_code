from typing import List

class FindDuplicates:
    
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if nums[abs(num) - 1] < 0: # since 1<=a[i]<=n, use abs(num) - 1 as the index of num; if it is negative, then seen before
                res.append(abs(num))
            nums[abs(num) - 1] *= -1 # elements only appear once or twice, not three times
        
        return res