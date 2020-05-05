# Version 1 of Binary Search
def binary_search(arr, elem):
    # we initialize two variables, one for the first/lowest indexed element
    # and one for the last/highest indexed element
    low = 0
    high = len(arr) - 1
    # While index 0 (low) is less than the last index (high) 
    while low <= high:
        # Mid is the middle index of the array
        mid = (low + high) // 2
        # Here we start our checks if the element at the middle index
        # is equal to, greater than, or less than the value that we're looking for.
        # If it's equal to it, then we just return the element at the middle index.
        if arr[mid] == elem:
            return mid
        # If the element at the middle index is greater than the element we're
        # looking for, then that element at the middle index will be our new highest element.
        elif arr[mid] > elem:
            high = mid - 1
        # If the element at the middle index is less than the element that
        # we're looking for then we initilaize the current element to be
        # the new lowest element and keep searching
        else:
            low = mid + 1
arr = [0, 1, 2, 8, 13, 17, 19, 32, 42]
elem = 32
print(binary_search(arr, elem)) # returns the index where the element is present