#!/usr/bin/python3
""" Finds Peak values """

def find_peak(list_of_integers):
    """Find the peak"""
    if len(list_of_integers) == 0:
        return None
    
""" binary search algorithim """


def binary_search(a, lo, hi):
    """Recursive binary search of the peak"""
    if lo >= hi:
        return lo
    mid = ((hi - lo) // 2) + lo
    if a[mid] > a[mid + 1]:
        return binary_search(a, lo, mid)
    else:
        return binary_search(a, mid + 1, hi)
