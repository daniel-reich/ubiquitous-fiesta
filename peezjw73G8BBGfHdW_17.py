
def arithmetic_operation(n):
  a = int(n.find(" "))
  b = int(n.rfind(" "))
  bb = ""
  c = 0
  d = 0
  for x in n:
    c = n[:a]
    d = n[b + 1:]
    bb = n[a + 1:b]
    if bb == "+":
      return int(c) + int(d)
    elif bb == "-":
      return int(c) - int(d)
    elif bb == "*":
      return int(c) * int(d)
    elif bb == "//":
      if int(d) == 0:
        return -1
      else:
        return int(c) // int(d)

