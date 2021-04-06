
def true_alphabetic(n):
  a = sorted(n.replace(" ", ""))
  b = ""
  c = 0
  for i in n:
      if i != " ":
          b += a[c]
          c += 1
      else: b += " "
  return b

