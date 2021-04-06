
def arrow(num):
  res = ['>'*i for i in range(1,num+1)]
  return res + res[::-1][num&1:]

