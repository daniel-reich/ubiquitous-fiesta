
def maya_number(n):
  res = []
  while n:
    res.insert(0, "o" * (n % 5) + "-" * (n // 5 % 4) or "@")
    n //= 20
  return res or ["@"]

