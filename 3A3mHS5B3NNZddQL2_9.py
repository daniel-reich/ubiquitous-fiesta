
from itertools import zip_longest
​
MAX = [5, 5, 10, 10, 15, 15, 20, 20]
​
def interview(lst, tot):
  return 'qualified' if all(a <= b for a, b in zip_longest(lst, MAX, fillvalue = float('inf'))) and tot <= 120 else 'disqualified'

