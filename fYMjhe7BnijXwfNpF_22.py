
def stmid(string):
  a = ""
  k = ""
  string += " "
  for letter in string:
    if letter != " ":
      a += letter
    else:
      if len(a) % 2 == 1:
        k += a[int(len(a)/2)]
      else:
        k += a[0]
      a = ""
  return k

