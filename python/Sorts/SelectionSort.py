def selection_sort(num_list):
    for i in range(len(num_list) - 1):
        min_index = i
        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[min_index]:
                min_index = j
        if i != min_index:
            temp = num_list[i]
            num_list[i] = num_list[min_index]
            num_list[min_index] = temp
    return num_list


print(selection_sort([4, 2, 5, 8, 1, 3, 2]))
