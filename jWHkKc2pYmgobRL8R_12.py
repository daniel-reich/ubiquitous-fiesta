
def distance_to_nearest_vowel(str):
  import numpy as np 
  l=[]
  vow=['a','e','i','o','u']
  for i in range(len(str)):
    if str[i] in vow:
      l.append(0)
    else:
      tmp=[]
      for j in range(len(str)):
        if str[j] in vow:
          tmp.append(j+1)
        else:
          tmp.append(3000)
      for k in range(len(tmp)):
          tmp[k]=np.abs(tmp[k]-(i+1))
      l.append(min(tmp))
  return l

