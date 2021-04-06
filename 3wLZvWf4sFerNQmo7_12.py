
def neutralise(s1, s2):
  k = ""
  i = 0
  while i < len(s1):
    if s1[i] == "+" and s2[i] == "+":
      k += "+"
    elif s1[i] == "-" and s2[i] == "-":
      k += "-"
    else:
      k += "0"
    i += 1
  return k

