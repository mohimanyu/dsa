# Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string.

# Note: The order of remaining characters in the output should be the same as in the original string.

# Example:

# Input: s = geeksforgeeks
# Output: geksfor
# Explanation: After removing duplicate characters such as e, k, g, s, we have string as "geksfor".

# Input: s = HappyNewYear
# Output: HapyNewYr
# Explanation: After removing duplicate characters such as p, e, a, we have string as "HapyNewYr".


def remove_duplicates(s):
    result = []
    seen = set()

    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)

    return "".join(result)


print(remove_duplicates("HappyNewYear"))
