
def remove_empty_arrays(arr):
    return [x for x in arr if not (type(x) == list and len(x) == 0)]

