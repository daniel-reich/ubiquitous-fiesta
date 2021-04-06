
from re import findall
​
def is_val_in_tree(tree, val):
    return val in [int(x) for x in findall(r"\d+", str(tree))]

