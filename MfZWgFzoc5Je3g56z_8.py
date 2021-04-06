
def translate(ran, num):
  arr=[x for x in range(ran**2+1)]
  k=ran**2-num
  if k in arr:
    i=0
    while arr[(num+i)%len(arr)]!=k:
      i+=1
    t=0
    while arr[num-t]!=k:
      t+=1
    if i<t or i==t==0:
      return "+{} ---> {}".format(i, k)
    elif i>t:
      return "-{} ---> {}".format(t, k)
    else:
      return "+{} or -{} ---> {}".format(i,t,k)
  else:
    return "{} is not in the range [0:{}]".format(num, ran**2)

