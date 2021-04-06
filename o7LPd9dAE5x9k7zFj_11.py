
def logarithm(base, num):
  for i in range(num):
    if base**i==num:
      return i
  else:
    return "Invalid"

