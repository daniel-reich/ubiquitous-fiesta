
def sum_of_holes(N):
  res = ""
  for k in range(1, N+1):
    res += str(k)
  return res.count("0")+res.count("4")+res.count("6")+res.count("9")+(res.count("8")*2)

