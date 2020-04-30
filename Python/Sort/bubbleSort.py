def bubbleSort(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

alist = [3, 8, 6, 7, 5, 4]

print(bubbleSort(alist))

def bubbleSortV2(arr):
    # default the swapped value to True
    swapped = True
    # Start the sorting loop
    while swapped:
        # set swapped to False
        swapped = False
        # for every element in the list
        for i in range(len(arr) - 1):
            # If this element is greater than the next element
            if arr[i] > arr[i + 1]:
                # Swap the values
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Print out that we've swapped these values
                print("Swapped: {} with {}".format(arr[i], arr[i + 1]))
                # Set swapped to True
                swapped = True
    # Finish up by returning our swapped list
    return arr

arr = [8, 2, 1, 3, 5, 4]
print(bubbleSortV2(arr))