
"""Given an unsorted list, create a function that returns the nth smallest element (the smallest element is the first
smallest, the second smallest element is the second smallest, etc)."""
​
​
def nth_smallest(lst, n):
    sorted_list = sorted(lst)
    for i in sorted_list:
        try:
            if sorted_list.index(i) + 1 == n: return i
        except ValueError:
            return "None"

