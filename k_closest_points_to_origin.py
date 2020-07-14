import heapq
from typing import List

class KClosestPointsToOrigin:

    # We keep a min heap of size K.
    # For each item, we insert an item to our heap.
    # If inserting an item makes heap size larger than k, then we immediately pop an item after inserting (heappushpop).

    # Runtime:
    # Inserting an item to a heap of size k take O(logK) time.
    # And we do this for each item points.
    # So runtime is O(N * logK) where N is the length of points.

    # Space: O(K) for our heap.
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = -(x * x + y * y) # default is min heap, so use negative to create max heap
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]
