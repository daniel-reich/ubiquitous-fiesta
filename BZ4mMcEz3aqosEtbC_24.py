
def mean(num):
  sum=0
  a=[int(i) for i in str(num)]
  for i in a:
    sum+=i
  return sum/len(a)

