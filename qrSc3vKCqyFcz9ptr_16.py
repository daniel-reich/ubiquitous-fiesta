
def sum_round(num):
  a = []
  for i, j in enumerate(str(num)[::-1]):
      if j!="0":
         a.append(j+i*"0")
  return " ".join(a)

