def productExceptSelf(arr):
    n = len(arr)
    prefProduct = [1] * n
    suffProduct = [1] * n
    res = [0] * n

    for i in range(1, n):
        prefProduct[i] = arr[i - 1] * prefProduct[i - 1]

    for j in range(n - 2, -1, -1):
        suffProduct[j] = arr[j + 1] * suffProduct[j + 1]

    for i in range(n):
        res[i] = prefProduct[i] * suffProduct[i]

    return res


arr = [10, 3, 5, 6, 2]
res = productExceptSelf(arr)
print(res)
# Output: [180, 600, 360, 300, 900]
