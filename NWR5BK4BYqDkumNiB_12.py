
from functools import reduce
​
divisible = lambda d, n: 0 if d is 0 else (n / d).is_integer()
prod = lambda lst: 0 if 0 in lst else reduce(lambda x, y: x * y, lst)
  
def digital_division(n):
    nums = list(map(int, str(n)))
    return ('Indivisible', 1, 2, 'Perfect')[sum((
        divisible(prod(nums), n),
        divisible(sum(nums), n),
        all(divisible(num, n) for num in nums if num != 0)
    ))]

