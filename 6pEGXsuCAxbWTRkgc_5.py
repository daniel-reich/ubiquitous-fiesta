
def loves_me(n):
  res = ["Loves me" + ["", " not"][i % 2] for i in range(n)]
  res[-1] = res[-1].upper()
  return ", ".join(res)

