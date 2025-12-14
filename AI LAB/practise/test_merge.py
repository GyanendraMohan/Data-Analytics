def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    leftArr = arr[low:mid+1]
    rightArr = arr[mid+1:high+1]

    i = 0
    j = 0
    k = low

    # Merge the two halves
    while i < n1 and j < n2:
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    # Copy remaining elements of leftArr, if any
    while i < n1:
        arr[k] = leftArr[i]
        i += 1
        k += 1

    # Copy remaining elements of rightArr, if any
    while j < n2:
        arr[k] = rightArr[j]
        j += 1
        k += 1


def mergesort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    size = len(arr)
    print(f"\nSize of the array is: {size}")
    print("\nOriginal array:", arr)
    mergesort(arr, 0, size - 1)
    print("\nSorted array:", arr)