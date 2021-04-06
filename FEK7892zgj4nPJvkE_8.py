
import math
​
​
def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for num_1 in range(2, int(math.sqrt(num))+1):
        if num % num_1 == 0:
            return False
    return True
​
​
​
​
​
def prime_gaps(g, a, b):
    if b - a < g:
        return None
    lst_prime = []
    for i in range(a, b+1):
       if is_prime(i):
          lst_prime.append(i)
          if len(lst_prime) >= 2 and i - lst_prime[-2] == g:
                return [lst_prime[-2], i]
    return None

