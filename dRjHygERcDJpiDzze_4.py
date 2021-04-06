
def lengthen(s1, s2):
  if(len(s1)<len(s2)):
    x=''
    x+=s1
    i=0
    while(len(s1)!=len(s2)):
      s1+=x[i]
      i+=1
      if(i>=len(x)):
        i=0
    return s1
  elif(len(s1)>len(s2)):
    x=''
    x+=s2
    i=0
    while(len(s2)!=len(s1)):
      s2+=x[i]
      i+=1
      if(i>=len(x)):
        i=0
    return s2

