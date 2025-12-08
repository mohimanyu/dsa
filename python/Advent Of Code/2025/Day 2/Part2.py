# --- Part Two ---
# The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

# From the same example as before:

# 11-22 still has two invalid IDs, 11 and 22.
# 95-115 now has two invalid IDs, 99 and 111.
# 998-1012 now has two invalid IDs, 999 and 1010.
# 1188511880-1188511890 still has one invalid ID, 1188511885.
# 222220-222224 still has one invalid ID, 222222.
# 1698522-1698528 still contains no invalid IDs.
# 446443-446449 still has one invalid ID, 446446.
# 38593856-38593862 still has one invalid ID, 38593859.
# 565653-565659 now has one invalid ID, 565656.
# 824824821-824824827 now has one invalid ID, 824824824.
# 2121212118-2121212124 now has one invalid ID, 2121212121.
# Adding up all the invalid IDs in this example produces 4174379265.

# What do you get if you add up all of the invalid IDs using these new rules?


def isRepeating(num: str):
    i = 0
    j = 1

    if len(num) % 2 == 0:
        j = len(num) % 2
    elif len(num) % 3 == 0:
        j = len(num) % 3
    else:
        while j + 1 < len(num):
            if num[i] == num[j] and num[i + 1] == num[j + 1]:
                break
            j += 1

    while j < len(num):
        if num[i] != num[j]:
            return False
        i += 1
        j += 1

    return True


rangeArr = "18623-26004,226779-293422,65855-88510,868-1423,248115026-248337139,903911-926580,97-121,67636417-67796062,24-47,6968-10197,193-242,3769-5052,5140337-5233474,2894097247-2894150301,979582-1016336,502-646,9132195-9191022,266-378,58-91,736828-868857,622792-694076,6767592127-6767717303,2920-3656,8811329-8931031,107384-147042,941220-969217,3-17,360063-562672,7979763615-7979843972,1890-2660,23170346-23308802"

rangeArr = rangeArr.split(",")
count = 0
for rangeLimit in rangeArr:
    limit = rangeLimit.split("-")

    for i in range(int(limit[0]), int(limit[1]) + 1):
        if isRepeating(str(i)) > 0:
            count += i

print(count)
