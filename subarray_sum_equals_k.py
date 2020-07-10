class SubarraySumEqualsK:

    # Whenever the sums has increased by a value of k, we've found a subarray of sums=k.
    # Include 0 so that when sums==k, it is accounted.
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = {}
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1

        return count