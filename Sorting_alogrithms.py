# This is the bubbleSort algorithm where we sort array elements from smallest to largest
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed (more efficient).

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1. Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Another bubble sort algorithm but returns the no. of times elements were swapped from small to large
def minimumSwaps(arr):
    swaps = 0
    temp = {}
    for i, val in enumerate(arr):
        temp[val] = i
    for i in range(len(arr)):
        # because they are consecutive, I can see if the number is where it belongs
        if arr[i] != i + 1:
            swaps += 1
            t = arr[i]  # Variable holder
            arr[i] = i + 1
            arr[temp[i + 1]] = t
            # Switch also the tmp array, no need to change i+1 as it's already in the right position
            temp[t] = temp[i + 1]
    return swaps


# A QuickSort algorithm where we pivot about a specified int in a array by partitioning the array into two parts
def quick_sort(sequence):
    if len(sequence)<=1:
        return(sequence)
    else:
        pivot = sequence.pop()
        
    items_bigger = []
    items_smaller = []
    for item in sequence:
        if item > pivot:
            items_bigger.append(item)
        else:
            items_smaller.append(item)
    return quick_sort(items_smaller) + [pivot] + quick_sort(items_bigger)


# This is the testing phase, where the above algorithms are tested and tried by FIRE🔥🔥🔥
testing_array = [3, 56, 0, 45, 2324, 2, 12, 123, 434, 670, 4549, 3, 4.5, 6]

print(bubbleSort(testing_array))
print(quick_sort(testing_array))
