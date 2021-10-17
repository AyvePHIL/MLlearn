import numpy as np
testing_array = [96, 54,100, 5500, 408356,85,0, 4,9,57]
# Bubblesorted to sort any array of numbers 
def bubblesort(x):
    for j in range(len(x)):

        for i in range(j):
            if x[i] > x[i + 1]:
                temp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = temp
    print(x)
    return x




def minimumSwaps(arr):
    swaps = 0
    temp = {}
    for i, val in enumerate(arr):
        temp[val] = i
    for i in range(len(arr)):
        # because they are consecutives, I can see if the number is where it belongs
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]     # Variable holder
            arr[i] = i+1
            arr[temp[i+1]] = t
            # Switch also the tmp array, no need to change i+1 as it's already good now
            temp[t] = temp[i+1]
    print(swaps)
    return(swaps)




# THIS ONE WORKS
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # print(arr)
    return(arr)
arr=testing_array
bubbleSort(arr)

A = np.array([[-0.23,  0.11],
              [0.29, -0.37]])
# Now use the number array and mutiply with a new one then sort again
print(A*6)