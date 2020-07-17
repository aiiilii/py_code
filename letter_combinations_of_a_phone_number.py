from typing import List

class LetterCombinations:

    def letterCombinations(self, digit: str) -> List[str]:
        res = []
        if len(digit) == 0:
            return res

        mappings = [
            ["0"],
            ["1"],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"]
        ]

        temp = ""
        self.backtracking(res, mappings, temp, digits)

        return res

    def backtracking(self, res: List[str], mappings: List[List[str]], temp: str, digits: str) -> None:
        if len(temp) == len(digits):
            res.append(temp)
            return

        for ch in mappings[int(digits[len(temp)])]:
            temp += ch
            self.backtracking(res, mappings, temp, digits)
            temp = temp[:-1] # splice to the one before the last digit