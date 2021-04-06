
from itertools import combinations
​
def two_product(lst, n):
  if len(lst) != 0:
    lst = sorted(lst)
    x = list(combinations(lst, 2))
    print(x)
    for i in range(len(x)):
      num1 = x[i][0]
      num2 = x[i][1]
      if num1 * num2 == n:
        return [num1, num2]

