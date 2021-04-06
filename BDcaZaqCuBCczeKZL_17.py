
def arrow(num):
  return ['>' * i for i in range (1,num+1) ]  + ['>' * i for i in reversed(range (1,num+1)) ] if not num%2 else ['>' * i for i in range (1,num) ]   + ['>' * i for i in reversed(range (1,num+1)) ]

