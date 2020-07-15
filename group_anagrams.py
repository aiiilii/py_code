from typing import List

class GroupAnagrams:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            key = tuple(sorted(w)) # tuple makes the w sequence immutable
            d[key] = d.get(key, []) + [w]
        return list(d.values())