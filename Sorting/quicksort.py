def quicksort(arr, left, right):
    if left < right:
        pivot = right
        partitionindex = partition(arr, pivot, left, right)

        quicksort(arr, left, partitionindex - 1)
        quicksort(arr, partitionindex + 1, right)

    return arr

def partition(arr, pivot, left, right):
    pivotvalue = arr[pivot]
    partitionindex = left

    for i in range(left, right):
        if arr[i] < pivotvalue:
            swap(arr, i, partitionindex)
            partitionindex += 1

    swap(arr, right, partitionindex)
    return partitionindex

def swap(arr, firstindex, secondindex):
    temp = arr[firstindex]
    arr[firstindex] = arr[secondindex]
    arr[secondindex] = temp

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
quicksort(numbers, 0, len(numbers)-1)
print(numbers)
    




