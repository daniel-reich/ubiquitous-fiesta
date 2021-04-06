
def funny_numbers(n, p):
  total = sum(int(i) ** (p + idx) for idx, i in enumerate(str(n)))
  return None if total % n else total // n

