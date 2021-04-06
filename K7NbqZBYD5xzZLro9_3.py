
import math
​
def digits_sum(start, stop):
  return sum_of_digits(stop) - sum_of_digits(start - 1)
​
def sum_of_digits(n):
  if n < 10:
    return (n * (n +1)) / 2
  d = int(math.log10(n))
  lst = [0] * (d + 1)
  lst[1] = 45
  for i in range(2, d + 1):
    lst[i] = lst[i - 1] * 10 + 45 * int(math.ceil(math.pow(10, i - 1)))
  p = int(math.ceil(math.pow(10, d)))
  msd = n // p
  return int(msd * lst[d] + (msd * (msd - 1) // 2) * p +
          msd * (1 + n % p) + sum_of_digits(n % p))

