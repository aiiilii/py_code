from typing import List

class Permutation:

    def permute(self, nums: List[int]) -> List[int]:
        
        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                res.append(nums[:])

            for i in range(first, n):
                # place i-th integer first in the current permutation
                # swap
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack (swap back)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


    def permute1(self, nums: List[int]) -> List[List[int]]:
        
        # can also pass the nums in as value not reference
        def backtrack(nums, first=0):
            if first == n:
                res.append(list(nums))
                return

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(list(nums), first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack(nums)
        return res


def main():
    nums = [1,2,3]
    p = Permutation()
    print(p.permute(nums))

if __name__ == "__main__":
    main()