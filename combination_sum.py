from typing import List

class CombinationSum:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates:
            return res

        candidates.sort()
        self.backtrack(res, candidates, [], target, 0)

        return res

    def backtrack(self, res: List[List[int]], candidates: List[int], templist: List[int], remain: int, start: int) -> None:
        if remain < 0:
            return
        elif remain == 0:
            res.append(templist)
            return
        else:
            for i in range(start, len(candidates)):
                self.backtrack(res, candidates, templist + [candidates[i]], remain - candidates[i], i)