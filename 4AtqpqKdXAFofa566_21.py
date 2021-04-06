
def remove_leading_trailing(n):
  if n.count("0") == len(n):
    return "0"
  elif n.count("0") == len(n) - 1 and "." in n:
    return "0"
  else:
    while True:
      if n[0] != "0" or n[1] == ".":
        break
      n = n[1::]
    while True:
      if n.count("0") == len(n):
        return "0"
        break
      if not "." in n:
        break
      if n[-1] != "0" and n[-1] != ".":
        break
      if n[-1] == ".":
        n = n[:-1]
        break
      n = n[:-1]
    return n

