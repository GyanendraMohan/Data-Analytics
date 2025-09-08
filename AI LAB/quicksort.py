import time
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def partition(arr, low, high):
    i = low
    j = high + 1
    pivot = arr[low] # considered first element as pivot

    while True:
        i += 1
        while i <= high and arr[i] < pivot:
            i += 1

        j -= 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j  

def quicksort(list, low, high):
    if low < high:
        pivot_position = partition(list, low, high)
        quicksort(list, low, pivot_position - 1)
        quicksort(list, pivot_position + 1, high )

def display(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print()


if __name__ == "__main__":
    list = [60,40,90,75,30,75,20,50,40]
    size = len(list)
    print(size)
    start = time.time()
    print("Given array is", list)
    quicksort(list,0,size-1)
    print("Sorted array is")
    end  = time.time()
    print("Time taken to sort the array is ", end - start)
    display(list)
    