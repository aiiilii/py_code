from typing import List

class MergeIntervals:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on the starting time
        intervals.sort(key = lambda x: x[0])

        merged = []

        for interval in intervals:
            # if merged is empty
            # or if the current interval does not overlap with the previous, then append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # else, there is overlap, so we merge the current and previous intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged