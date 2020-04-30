"""
Pure implementation of insertion sort in python
:param collection: mutable ordered collection with heterogenous comparable items inside
:return: the same collection ordered by ascending
"""

def insertion_sort(collection):
    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        while (insertion_index > 0 and collection[insertion_index - 1] > collection[insertion_index]):
            collection[insertion_index], collection[insertion_index - 1] = (collection[insertion_index - 1], collection[insertion_index])
            insertion_index -= 1

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a space:\n").strip()
    unsorted = [int(item) for item in user_input.split(" ")]
    print(insertion_sort(unsorted))