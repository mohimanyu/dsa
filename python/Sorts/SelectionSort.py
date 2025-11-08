def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(selection_sort([4, 2, 5, 8, 1, 3, 2, 0]))
