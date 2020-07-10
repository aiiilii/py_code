class VerifyingAnAlienDictionary:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Find the first difference word1[k] != word2[k].
            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break # do not need to return false if the above if-statement is false, that means they letters do not equal at k,
                        # just break out and check the next two words

            # for/else statement: else is called if the corresponding for loop does not hit a BREAK at any point. 
            # https://book.pythontips.com/en/latest/for_-_else.html
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

        return True