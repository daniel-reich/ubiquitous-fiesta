
def count(n):
  digits, number = 0, abs(n)
  while number > 0:
    number //= 10
    digits += 1
  return 1 if abs(n) < 10 else digits

