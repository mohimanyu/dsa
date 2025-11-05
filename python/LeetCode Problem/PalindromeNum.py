def isPalindrome(x: int) -> bool:
    # checking for negative value
    if x < 0:
        return False

    # reverse x
    reverse_x = int(str(x)[::-1])

    # palindrome check
    if x == reverse_x:
        return True
    return False


print(isPalindrome(121))
