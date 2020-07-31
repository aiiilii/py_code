from typing import List
import collections

class FindAllAnagrams:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)

        if ns < np:
            return []

        p_count = collections.Counter(p)
        s_count = collections.Counter()

        res = []

        # sliding window on string s
        for i in range(ns):
            # add one more letter on the right side of the window in to the counter
            s_count[s[i]] += 1

            # remove one letter on the left side of the window
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1

            # compare the counter dict in the sliding window to with the reference counter dict
            if p_count == s_count:
                res.append(i - np + 1)

        return res