#!/usr/bin/python3

def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): the list of integers to find the peak in

    Usage:
         >> find_peak([0, 1, -1, 7, 5])
         >> 7
    """

    if list_of_integers == []:
        return None

    length_of_list = len(list_of_integers)
    if length_of_list == 1:
        return list_of_integers[0]
    if length_of_list == 2:
        return max(list_of_integers)

    half_of_length = int(length_of_list / 2)
    peak = list_of_integers[half_of_length]
    if peak > list_of_integers[half_of_length - 1] \
            and peak > list_of_integers[half_of_length + 1]:
        return peak
    elif peak > list_of_integers[half_of_length + 1]:
        return find_peak(list_of_integers[:half_of_length])
    else:
        return find_peak(list_of_integers[half_of_length + 1:])
