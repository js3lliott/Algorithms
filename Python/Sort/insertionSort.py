def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        position = i
        # Move elements of arr[0...i-1], that are
        # greater than current, to one position ahead
        # of their current position

        while position > 0 and arr[position - 1] > current:
            print("Swapped {} for {}".format(arr[position], arr[position-1]))
            arr[position] = arr[position - 1]
            print(arr)
            position -= 1
            
        arr[position] = current
    return arr

arr = [8, 2, 1, 3, 5, 4]
print(insertionSort(arr))