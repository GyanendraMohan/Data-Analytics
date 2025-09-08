def merge(arr, low, mid, high):
    n1 = mid - low + 1  # size of left half
    n2 = high - mid     # size of right half

    # create temporary arrays
    leftArr = arr[low:mid+1]
    rightArr = arr[mid+1:high+1]

    i = 0  # index for leftArr
    j = 0  # index for rightArr
    k = low  # index for main arr

    # merge the two halves
    while i < n1 and j < n2:
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    # copy remaining elements of leftArr, if any
    while i < n1:
        arr[k] = leftArr[i]
        i += 1
        k += 1

    # copy remaining elements of rightArr, if any
    while j < n2:
        arr[k] = rightArr[j]
        j += 1
        k += 1



def mergesort(arr, low, high):
    if low < high :
        mid = (low + high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        merge(arr, low , mid , high)        

if __name__ == "__main__":
    arr = [60,40,90,75,30,75,20,50,40]
    size = len(arr)
    mergesort(arr, 0 , size-1)
    print("Sorted array : ", arr)