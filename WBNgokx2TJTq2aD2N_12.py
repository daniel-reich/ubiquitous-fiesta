
def smallest(digits, value):
  n = int("1" + "0" * (digits-1 ))
  if n % value == 0: return n
  return n + value - (n % value)

