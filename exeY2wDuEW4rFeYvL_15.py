
def ordered_matrix(a, b):
  nums = [i for i in range(1, a*b + 1)]
  return [[nums.pop(0) for _ in range(b)] for _ in range(a)]

