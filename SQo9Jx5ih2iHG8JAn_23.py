
def expanded_form(num):
  num=str(num)[::-1]
  ans=[]
  for i in range(len(num)):
    if num[i]!='0':ans.append(num[i]+'0'*i)
  return ' + '.join(ans[::-1])

