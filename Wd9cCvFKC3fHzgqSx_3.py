
def num_split(num):
  if num>=0:
    count=len(str(num))-1
    lst=[]
    for i in str(num):
      lst.append(int(i)*(10**count))
      count=count-1
  if num<0:
    num=num*(-1)
    count=len(str(num))-1
    lst=[]
    for i in str(num):
      lst.append((-1)*int(i)*(10**count))
      count=count-1
  return lst

