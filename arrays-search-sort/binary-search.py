

# def binarySearch(arr, target, left, right):
#     if left > right:
#         return "Cannot find"
#     mid = left + right // 2
#     if arr[mid] < target:
#         binarySearch(arr, target, mid+1, right)
#     elif arr[mid] == target:
#         return mid
#     else:
#         binarySearch(arr, target, 0, mid-1)


def binarySearch(arr, target):
    left = 0
    right = len(arr)-1

    while(left <= right):
        mid = left + right // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    arr = [1, 2, 3, 4, 5, 6]
    target = 6
    print(binarySearch(arr, target))


if __name__ == "__main__":
    main()
