
def amplify(num):
  result=[]
  n=1
  while n<num+1:
    if not n%4:
      result.append(n*10)
    else:
      result.append(n)
    n+=1
  return result

