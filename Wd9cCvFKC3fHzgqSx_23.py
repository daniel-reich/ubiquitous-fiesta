
def num_split(num):
  ret = []
  neg = num//abs(num)
  num = str(abs(num))[::-1]
  for i in range(len(num)):
    ret.append(int(num[i])*(10**i)*neg)
  return ret[::-1]

