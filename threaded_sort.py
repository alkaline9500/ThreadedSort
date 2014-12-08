"""
Threaded Sort
"""

__author__ = "Nic Manoogian"

from multiprocessing import Pool, cpu_count
from random import randint
from time import time

def merge(lists):
    """
    Merges a list of lists and returns the min-merged list
    """
    merged_list = []
    if len(lists) == 0:
        return merged_list
    min_list = lists[0]
    while min_list != None:
        min_list = None
        for l in lists:
            if len(l) == 0:
                continue
            if not min_list or l[0] < min_list[0]:
                min_list = l
        if min_list != None:
            merged_list.append(min_list.pop(0))
    return merged_list

def threaded_sort(elements):
    """
    Uses a thread pool to sort elements
    """
    # Let's see what we're working with
    group_count = cpu_count()

    # Don't bother using threads if we can't put
    # at least 5 things into each group
    if len(elements) <= group_count*5:
        return sorted(elements)
    groups = [elements[i:i+group_count] for i in range(0, len(elements), group_count)]
    return merge(Pool().map(sorted, groups))

if __name__ == "__main__":
    elements = [randint(0, 100000) for _ in range(10000)]
    print("Non-threaded")
    start = time()
    regular = sorted(elements)
    print(time()-start)

    print("Threaded")
    start = time()
    threaded = threaded_sort(elements)
    print(time()-start)

    print("Valid: {b}".format(b=(str(regular) == str(threaded))))

