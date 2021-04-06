
def arrow(num):
  if num % 2 == 0:
    return [">"*i for i in range(1,num+1)]+[">"*i for i in reversed(range(1,num+1))]
  return [">"*i for i in range(1,num+1)]+[">"*i for i in reversed(range(1,num))]

