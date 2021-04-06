
def reversed_binary_integer(num):
  res=bin(num)
  res=res[2::]
  sum=0
  for i,v in enumerate(res):
    sum=sum+(int(v)*2**i)
  return sum

