
from math import log10 as log
# takes a number and returns the sum of its digits
sum_dig = lambda n: sum(list(map(int, str(n))))
​
# takes start and finish and returns sum over small range
small_sum = lambda s, f: sum(sum_dig(n) for n in range(s, f+1))
                         
def digits_sum(s, f):
    sum_start = small_sum(0, s - 1)
    digit_count = int(log(f))
    powers = [4.5 * n * 10 ** n for n in range(digit_count + 1)]
    closest_9s = int(digit_count * '9') if digit_count > 0 else 0
    return powers[digit_count] + small_sum(closest_9s + 1, f) - sum_start

