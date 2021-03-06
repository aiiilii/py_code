from typing import List

class IntervalListIntersections:

    def intervalIntersections(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0

        while i < len(A) and j < len(B):
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])

            if low <= high:
                res.append([low, high])

            if A[i][1] <= B[j][1]:
                i += 1
            else:
                j += 1

        return res