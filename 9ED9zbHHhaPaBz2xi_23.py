
def normal_sequence(n):
  lst = [0, 1, 1, 2, 0, 2, 2, 1]
  return lst[n % 8 - 1] if n % 8 else 1

