from typing import List

class MergeSortedArray:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2] # put the larger number towards the back
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
    
        # add the missing elements from nums2
        # if nums2 exhausts first, then p2 would equal to -1, and nums2[:-1 + 1] == nums2[:0], which means nums1[:0] = [] (empty list), which does nothing
        nums1[:p2 + 1] = nums2[:p2 + 1]