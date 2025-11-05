def findMedianSortedArrays(nums1, nums2) -> float:
    # merging the two lists
    merged_arr = nums1 + nums2

    # sorting the merged list
    merged_arr.sort()

    # calculate length of merged_arr
    length = len(merged_arr)

    # operating based on length of the merged list
    if length % 2 == 0:
        return (merged_arr[(length // 2) - 1] + merged_arr[(length // 2)]) / 2
    else:
        return merged_arr[(length // 2)]


print(findMedianSortedArrays([1, 2], [3]))
