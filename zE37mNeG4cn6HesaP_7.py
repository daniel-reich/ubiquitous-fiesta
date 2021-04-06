
def max_ham(s1, s2):
 # check if anagram
 s2_lst=list(s2)
 #print(s2_lst)
 for i in range(0,len(s1)):
  if s1[i] in s2_lst:
   s2_lst.pop(s2_lst.index(s1[i]))
  else:
   return False
 if len(s2_lst) != 0:
  return False
 # if is anagram
 # check hamming distance
 dist=0
 for k in range(0,len(s1)):
  if s1[k] != s2[k]:
   dist+=1
 # if hamming distance < len of strings
 if dist < len(s1):
  return dist
 else:
  return True

