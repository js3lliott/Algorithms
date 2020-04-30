# This is a master file for various versions of sorting algorithms implemented in Python

# Version 1 of Merge Sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # We will recursively call the mergeSort function
        # on both the left half and the right half of the 
        # array until we reach the base cases (len(arr) = 1)
        mergeSort(left)
        mergeSort(right)

        # We initialize pointers for traversal of the left 
        # and right half of the arrays as well as a third
        # pointer for inserting and sorting the values in
        # the original array
        i = 0
        j = 0
        k = 0

        # While the pointers haven't reached the end of
        # the arrays
        while i < len(left) and j < len(right):
            # if the value in the left array at position i
            # is less than the value at position j
            # in the right array
            if left[i] <= right[j]:
                arr[k] = left[i]
                # increase the left pointer by one
                i += 1
            
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # We'll create two other while loops just in case
        # one of the arrays rusn out of values to traverse
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [6, 2, 4, 1, 3, 7, 5, 8]
mergeSort(arr)
print(arr)


# Version 1 of Quick Sort
# O(n^2) time

def quickSort(nums):

    # We'll create a helper function that recursively
    # sorts the array for everything below the pivot value
    # and verything above the pivot value
    quickSortHelper((nums, 0, len(nums) - 1))
    
    # Now we'll define the quickSortHelper function
    def quickSortHelper(nums, first, last):
        # if our "first" index pointer is less than our
        # "last" index pointer
        if first < last:
            # we'll use a partition function to find a pivot
            # value in the array and assign it to a variable
            # for easier access
            split = partition(nums, first, last)

            # Recursively call the helper function on values
            # below the pivot value and vlaues above the pivot
            quickSortHelper(nums, first, split - 1)
            quickSortHelper((nums, split + 1, last))

    def partition(nums, first, last):
        # The pivot value can be anything in the array really
        # but usually it can be the first value in the array
        pivot_value = nums[first]

        # create a left pointer and a right pointer
        # the left pointer has to be the value right after
        # "pivot" which is the first value specified
        left_point = first + 1
        right_point = last

        # Create a check point for the array being sorted/done
        done = False
        while not done:
            
            # This while loop checks that the left pointer index is less than
            # the right pointer index and that the value at the left pointer index
            # is less than the pivot value. If everything checks out then we increment
            # the left pointer
            while left_point <= right_point and nums[left_point] <= pivot_value:
                left_point = left_point + 1

            # This while loop checks that the right pointer index is greater than
            # the left pointer index and that the value at the right pointer index
            # is greater than the pivot value. If everything checks out then we decrement
            # the right pointer
            while right_point >= left_point and nums[right_point] >= pivot_value:
                right_point = right_point - 1

            # When the right pointer is pointing at an index
            # value less than the left pointer index then
            # we are done traversing the list
            if right_point < left_point:
                done = True
            # If none of the while loops check out and the 
            # right pointer isn't at a value less than
            # the left pointer then we need to swap them
            # since they are in the wrong positions
            else:
                temp = nums[left_point]
                nums[left_point] = nums[right_point]
                nums[right_point] = temp

        temp = nums[first]
        nums[first] = nums[right_point]
        nums[right_point] = temp

        return right_point
nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(nums)
print(nums)

