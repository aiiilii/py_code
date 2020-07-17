import heapq

class KthLargestElement:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # .nlargest(k, nums) return an iterable that is the largest k number from nums
        #[-1] return the last element, which is the kth largest
        return heapq.nlargest(k, nums)[-1]