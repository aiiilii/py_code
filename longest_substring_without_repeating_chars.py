class LongestSubstring:

    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}

        start = 0
        max_length = 0

        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1 # used[c] is the location of the previously stored c, it is not the current c we are looking at
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length
