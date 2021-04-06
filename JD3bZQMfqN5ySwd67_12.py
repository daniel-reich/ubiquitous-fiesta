
from itertools import permutations as pt
​
​
def is_vampire(n):
    if n < 100:
        return 'Normal Number'
    lst = list(pt(list(str(n))))
    len_n = len(str(n))
    half_len = len_n // 2
    product_equal = False
    for tpl in lst:
        left = int(''.join(tpl[i] for i in range(half_len)))
        right = int(''.join(tpl[i] for i in range(half_len, len_n)))
        if left * right == n:
            product_equal = True
    if len_n % 2 and product_equal:
        return 'Pseudovampire'
    elif product_equal:
        return 'True Vampire'
    else:
        return 'Normal Number'

