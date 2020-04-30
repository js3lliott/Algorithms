def bubble_sort(collection):
    """
    Implementation of bubble sort in Python
    :param: collection: some mutable ordered collection with heterogenous comparable items inside
    :return: the same collection ordered by ascending
    """

    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break # Stop iteration if the collection is sorted

    return collection

if __name__ == "__main__":

    user_input = input("Enter numbers separated by a comma: ").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*bubble_sort(unsorted), sep=",")