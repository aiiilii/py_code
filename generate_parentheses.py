from typing import List

class GenerateParentheses:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        if n == 0:
            return res

        templist = ''
        self.backtracking(res, templist, 0, 0, n)

        return res

    def backtracking(self, res: List[str], templist: str, left: int, right: int, max_paren: int) -> None:
        if len(templist) == max_paren * 2:
            res.append(templist) # same as (res += [templist])
            return

        if left < max_paren:
            self.backtracking(res, templist + '(', left + 1, right, max_paren)

        if right < left:
            self.backtracking(res, templist + ')', left, right + 1, max_paren)