def linear_search(arr, target):
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1   # not found


def binary_search(arr, target):
    left = 0
    right = len(arr)
    while right > left:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid
        elif arr[mid] < target:
            left = mid
    return -1  # not found
