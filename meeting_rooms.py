from typing import List

class MeetingRooms:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) < 2 or len(intervals[0]) != 2:
            return True

        intervals.sort(key = lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True