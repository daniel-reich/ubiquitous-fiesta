
def id_mtrx(n):
  try:
    res = []
    for i in range(abs(n)):
      res += [[0 for j in range(abs(n)-i-1)]+[1]+[0 for j in range(i)]]
    if n>0:
      return res[-1::-1]
    return res
  except:
    return "Error"

