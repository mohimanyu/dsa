def bubble_sort(num_list):
    for i in range(len(num_list) - 1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j + 1]:
                temp = num_list[j]
                num_list[j] = num_list[j + 1]
                num_list[j + 1] = temp
    return num_list


print(bubble_sort([4, 2, 5, 8, 1, 3, 2]))
