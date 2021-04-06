
def super_digit(n, k):
  nstr = ""
  for each in range(k):
    nstr += n
  while True:
    if len(nstr) == 1:
      return int(nstr)
      break
    else:
      sumn = 0
      for i in nstr:
        sumn += int(i)
      nstr = str(sumn)

