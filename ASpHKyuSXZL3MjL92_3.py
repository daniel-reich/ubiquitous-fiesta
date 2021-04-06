
def amplify(num):
  out= []
  for i in range(1,num+1):
    if i % 4 ==0:
      i = i * 10  
    out.append(i)
  return out

