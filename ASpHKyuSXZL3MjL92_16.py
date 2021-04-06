
def amplify(num):
  lst = list(range(1,num+1))
  for i in lst:
    if not i%4:
      lst[i-1]=10*i
  return lst

