# Given a string s, return the longest palindromic substring in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"


# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longPStr = ""
        currStr = ""

        for char in s:
            currStr += char

            for k in range(len(currStr)):
                window = currStr[k:]
                if window == window[::-1]:
                    if len(window) > len(longPStr):
                        longPStr = window
                        break

        return longPStr


lpstr = Solution()
print(lpstr.longestPalindrome("cbbd"))  # Output: bb
print(lpstr.longestPalindrome("babad"))  # Output: bab
