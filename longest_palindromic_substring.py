class LongestPalindrome:

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp
            
            # even case, like "abba"
            temp = self.helper(s, i, i + 1)
            if len(temp) > len(res):
                res = temp

        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1 # move leftward from the left
            r += 1 #move rightward from the right

        return s[l+1:r] # return what is before the end of the while loop on both the left and right sides
