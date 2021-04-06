
import math
​
​
def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for num_1 in range(2, int(math.sqrt(num)) + 1):
        if num % num_1 == 0:
            return False
    return True
​
​
def sum_prime(lst):
    result = ""
    for i in range(2, lst[-1]+1):
        if is_prime(i):
            sum_prime = 0
            for num in lst:
                if num % i == 0:
                    sum_prime += num
            if sum_prime != 0:
                result += "({} {})".format(i, sum_prime)
    return result

