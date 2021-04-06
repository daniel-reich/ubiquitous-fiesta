
def func(num):
  count=0
  for i in str(num):
    count+=(int(i)-len(str(num)))
  return count

