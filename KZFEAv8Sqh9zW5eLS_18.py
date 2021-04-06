
from copy import deepcopy
def flatten_list(nested_list):
    nested_list = deepcopy(nested_list)
​
    while nested_list:
        sublist = nested_list.pop(0)
​
        if isinstance(sublist, list):
            nested_list = sublist + nested_list
        else:
            yield sublist
​
def is_val_in_tree(lst, num):
    if num in flatten_list(lst):
        return True
    return False

