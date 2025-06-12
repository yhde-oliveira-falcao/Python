arr = ['a', 'b', 'c', 'x', 'y', 'z']

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found

arr1 = [1, 3, 5, 7, 9, 11]
target = 7
print(binary_search(arr1, target))