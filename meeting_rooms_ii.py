from typing import List

class MeetingRoomsII:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0 or len(intervals[0]) != 2:
            return 0

        start = []
        end = []

        for i in range(len(intervals)):
            start.append([intervals[i][0]])
            end.append([intervals[i][1]])

        start.sort()
        end.sort()

        res = 0
        end_point = 0

        for i in range(len(start)):
            if start[i] < end[end_point]: # if started a room before an end
                res += 1
            else: # if not intercepting the previous start-end range
                end_point += 1

        return res