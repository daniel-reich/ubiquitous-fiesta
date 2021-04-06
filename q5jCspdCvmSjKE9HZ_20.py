
from functools import reduce
lcm = lambda a, b: a * lcm(b, a % b) / (a % b) if a % b else a
def lcm_of_list(numbers): return reduce(lcm, numbers)

