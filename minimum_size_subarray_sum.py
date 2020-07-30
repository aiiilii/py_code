from typing import List

class MinSizeSubarraySum:
    
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                res = min(res, i - left + 1) # Update res=min(res,i+1−left), where i−left+1 is the size of current subarray
                sum -= nums[left] # subtract nums[left] from sum and increment left
                left += 1

        return res if res != float('inf') else 0