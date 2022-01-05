
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        # Last i elements in place after ith pass
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        # First i elements in place after ith pass
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        # Move minimum unsorted element to front
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def mergeSort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0  # Left half crawler
        j = 0  # Right half crawler
        k = 0  # Sorted array index

        # Sort and copy left and right
        while i < len(left) & j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Fill in remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def main():
    print("Main:")
    arr = [64, 34, 25, 12, 22, 11, 90]
    # bubbleSort(arr)
    # selectionSort(arr)
    mergeSort(arr)
    print("Sorted Array: ", arr)


if __name__ == "__main__":
    main()
