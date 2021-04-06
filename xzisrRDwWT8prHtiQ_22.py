
def difference_two(lst):
    """
    Return pairs of integers that have a difference of two.
​
    Args:
        lst (List[int]): Assume there are no duplicate integers in the array.
        The order of the integers in the input array should not matter.
​
    Returns:
        List[List[int]]: Sorted in ascending order of values
    """
    lst.sort(reverse=True)
    res_lst = []
    for i in lst:
        for j in lst:
            if i - j == 2:
                res_lst.append([j, i])
                continue
    return list(reversed(res_lst))

