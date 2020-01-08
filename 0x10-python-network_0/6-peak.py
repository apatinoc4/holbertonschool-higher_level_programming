#!/usr/bin/python3
# Write a function that finds a peak in a list of unsorted integers


def find_peak(list_of_integers):
    """ find_peak main function """
    if not list_of_integers:
        return None
    return finder(list_of_integers, len(list_of_integers),
                  0, len(list_of_integers) - 1)


def finder(array, length, low, high):
    """ find peak helper function """
    mid = low + (high - low) // 2
    if ((mid == 0 or array[mid] >= array[mid - 1]) and
            (mid == length - 1 or array[mid] >= array[mid + 1])):
        return array[mid]
    elif mid > 0 and array[mid - 1] > array[mid]:
        return finder(array, length, low, mid - 1)
    else:
        return finder(array, length, mid + 1, high)
