
import itertools
def check_sum(lst, n):
  return any(sum(num) == n for num in itertools.combinations(lst, 2))

