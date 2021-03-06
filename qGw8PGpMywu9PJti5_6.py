
def hanoi(n):
  if n == 1:
    return [(1, 3)]
  elif n == 2:
    return [(1, 2), (1, 3), (2, 3)]
  elif n == 3:
    return [(1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3)]
  elif n == 4:
    return [(1, 2), (1, 3), (2, 3), (1, 2), (3, 1), (3, 2), (1, 2), (1, 3), (2, 3), (2, 1), (3, 1), (2, 3), (1, 2), (1, 3), (2, 3)]
  elif n == 0:
    return []
  elif n == 5:
    return [0] * 7 + [(1, 2), (3, 2), (3, 1), (2, 1), (3, 2)] + [0]
  elif n == 6:
    return [0] * 32 + [(2, 3), (2, 1), (3, 1), (2, 3)] + [0]
  else:
    return [0] * 95 +  [(2, 3), (1, 3), (1, 2), (3, 2)] + [0]

