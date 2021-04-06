
def longest_run(lst):
    '''A consecutive-run is a list of adjacent, consecutive integers.
  This list can be either increasing or decreasing. 
  Create a function that takes a list of integers
  and returns the length of the longest consecutive-run.'''
    from itertools import groupby
    ones = list(len(tuple(x[1])) for x in groupby(x - y for x, y in zip(lst, lst[1:])) if abs(x[0]) == 1)
    if len(ones) < 1: return 1
    return max(ones) + 1

