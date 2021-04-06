
def get_sequence(low, high):
  if low == high:
    return [low]
  return [i for i in range(low,high + 1)]

