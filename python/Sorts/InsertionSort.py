def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        temp = num_list[i]
        j = i - 1
        while temp < num_list[j] and j >= 0:
            num_list[j + 1] = num_list[j]
            num_list[j] = temp
            j -= 1
    return num_list


print(insertion_sort([4, 2, 5, 8, 1, 3, 2]))
