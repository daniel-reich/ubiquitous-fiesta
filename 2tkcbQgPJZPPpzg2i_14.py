
def sum_of_holes(N):
  num=''
  for i in range(1,N+1):
    num=num+str(i)
  return num.count("4") + num.count("6")+num.count("8")*2 + num.count("9")+num.count("0")

