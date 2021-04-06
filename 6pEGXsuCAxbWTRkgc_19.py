
def loves_me(n):
  if n == 1:
    return "LOVES ME"
  phrase = "Loves me"
  for i in range(1, n - 1):
    if i % 2 == 0:
      phrase += ", Loves me"
    else:
      phrase += ", Loves me not"
  if n % 2 == 0:
      phrase += ", LOVES ME NOT"
  else:
      phrase += ", LOVES ME"
  return phrase

