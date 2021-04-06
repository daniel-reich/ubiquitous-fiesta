
def loves_me(n):
  l = ["Loves me not" if i%2 else "Loves me" for i in range(n)]
  l[-1] = l[-1].upper()
  return ", ".join(l)

