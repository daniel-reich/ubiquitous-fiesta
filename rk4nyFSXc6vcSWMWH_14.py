
def shared_digits(n):
  return all(False for i, j in zip(n, n[1:]) if not len(set(str(i)) & set(str(j))) >= 1)

