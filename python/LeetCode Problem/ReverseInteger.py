def reverse(x: int) -> int:
    # determining sign
    sign = -1 if x < 0 else 1

    # abs(x)
    x = abs(x)

    # reverse x
    reverse_x = int(str(x)[::-1])

    # reapply sign
    reverse_x *= sign

    # checking if reverse x is in range
    MAX_INT = 2**31 - 1
    MIN_INT = -(2**31)
    if reverse_x > MAX_INT or reverse_x < MIN_INT:
        return 0

    return reverse_x


print(reverse(-123))
