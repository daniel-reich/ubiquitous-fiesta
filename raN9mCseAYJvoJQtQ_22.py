
def remove_empty_arrays(arr):
    return [x for x in arr if not isinstance(x, list) or not len(x) == 0]

