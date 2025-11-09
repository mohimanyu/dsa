# Given a sorted and rotated array arr[] of distinct elements, find the index of given key in the array. If the key is not present in the array, return -1.

# Examples:

# Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
# Output: 8
# Explanation: 3 is present at index 8.

# Input: arr[] = [3, 5, 1, 2], key = 6
# Output: -1
# Explanation: 6 is not present.

# Input: arr[] = [33, 42, 72, 99], key = 42
# Output: 1
# Explanation: 42 is found at index 1.


def search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == key:
            return mid

        # If Left half is sorted
        if arr[mid] >= arr[left]:
            if key >= arr[left] and key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If Right half is sorted
        else:
            if key > arr[mid] and key <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 10
print(search(arr, key))
