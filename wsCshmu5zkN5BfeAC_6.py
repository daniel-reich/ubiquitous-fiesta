
def divisible_by_left(n):
  res = [False]
  str_n = str(n)
  for i in range(1,len(str_n)):
    if str_n[i - 1] == '0':
      res.append(False)
    else:
      res.append(int(str_n[i]) % int(str_n[i - 1]) == 0)
  return res

