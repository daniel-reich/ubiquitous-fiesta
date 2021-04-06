
def arrow(num):
  half = ['>'*i for i in range(1,num+1)]
  return half + half[::-1][num%2:]

