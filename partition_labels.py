from typing import List

class PartitionLabels:

    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)} # saves the last index of the ocurring char, overrides the previously saved index for each char
        j = 0
        anchor = 0
        res = []

        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                res.append(i - anchor + 1)
                anchor = i + 1

        return res

def main():
    S = "abjabcbacadefegdehijhklij"
    pl = PartitionLabels()
    print(pl.partitionLabels(S))

if __name__ == "__main__":
    main()