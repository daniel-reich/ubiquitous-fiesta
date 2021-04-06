
def amplify(num):
  lst = []
  for i in range(1,num+1):
    if i%4==0:
      lst.append(i*10)      
    else:
      lst.append(i)
  return(lst)

