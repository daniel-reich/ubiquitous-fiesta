
import numpy as np
def pyramidal_string(string, _type):
  string_len=[]
  n=len(string)
  s2=(-1+np.sqrt(1+8*n))/2
  pyramid=[]
  
  def concat_reg(n,string_):
    marche=""
    i0=int(n/2*(n+1))
    for i in range(n+1):
      marche+=(string_[i0+int(i)])
      marche+=(" ")
    return(marche[:-1])
  def concat_rev(n,string_):
    marche=""
    n0=len(string)-1
    i0=int(n/2*(n+1))
    for i in range(n+1):
      marche+=(string_[n0-i0-int(i)])
      marche+=(" ")
    return(marche[:-1])
  if n==0:
    pyramid=[]
    msg=pyramid
  elif n==1:
    pyramid.append(string[0])
    msg=pyramid
  elif (s2<0 or s2%1!=0) and n!=0 :
    msg ="Error!"
    
  elif s2>0 and n!=1:
    if _type == "REG":
        for i in range(int(s2)):
          pyramid.append(concat_reg(int(i),string))
        msg=pyramid
    elif _type == "REV":
        for i in range(int(s2)):
          pyramid.append(concat_rev(int(i),string))
        for i in range(len(pyramid)):
          pyramid[i]=pyramid[i][::-1] 
        pyramid.reverse()
        msg=pyramid
        
  return(msg)

