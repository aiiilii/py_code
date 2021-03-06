class MinimumRemove:

    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []

        for i, c in enumerate(s):
            if c not in "()":
                continue

            if c == "(":
                stack.append(i) # append the index into the stack
            elif not stack: # else if: c == ")" and stack is empty
                indexes_to_remove.add(i)
            else: #else: c == ")" and stack is not empty
                stack.pop()

        indexes_to_remove = indexes_to_remove.union(set(stack)) # combine the indexes_to_remove indexes and the indexes left inside the stack
        string_builder = []

        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)

        return "".join(string_builder)