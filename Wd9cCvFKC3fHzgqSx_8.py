
def num_split(num):
  l = []
  
  if str(num)[0] == "-": 
    for i in range(1, len(str(num))): 
      l.append(int("-"+str(num)[i]+"0"*(-1-i+len(str(num)))))
  else: 
    for i in range(0, len(str(num))): 
      l.append(int(str(num)[i]+"0"*(-1-i+len(str(num)))))
  return l

