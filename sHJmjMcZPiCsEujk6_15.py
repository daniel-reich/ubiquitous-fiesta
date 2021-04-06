
def pilish_string(n):
  pi="314159265358979"  
  if(len(n)<int(pi[0])):
    return n*(int(pi[0])-len(n)+1)
  
  ans=''
  j=0
  i=0
  while(j<len(n) and i<len(pi)):
    if(len(n[j:j+int(pi[i])])==int(pi[i])):
      ans+=n[j:j+int(pi[i])]+' '
    elif(len(n[j:j+int(pi[i])])<int(pi[i])):
      z=n[j:j+int(pi[i])]
      c=z[len(z)-1]
      while(len(z)<=int(pi[i])):  
        z+=c
      ans+=z
    j+=int(pi[i])   
    i+=1
  return ans[0:len(ans)-1]

