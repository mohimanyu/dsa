# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


# Constraints:

# -231 <= x <= 231 - 1


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        x = abs(x)

        revInt = int(str(x)[::-1])

        revInt *= sign

        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)
        if revInt > MAX_INT or revInt < MIN_INT:
            return 0

        return revInt


revInt = Solution()
print(revInt.reverse(-123))
