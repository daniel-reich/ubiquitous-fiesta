
import numpy as np
​
def get_products(lst):
    return [np.prod(np.array(lst[:i] + lst[i+1:])) for i in range(len(lst))]

