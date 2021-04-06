
def sum_round(num):
  num=str(num)
  ans=[]
  for i in range(len(num)):
    if num[i]!='0':
      ans.append(num[i]+('0'*(len(num[i:])-1)))
  return ' '.join(ans[::-1])

