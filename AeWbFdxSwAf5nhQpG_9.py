
# Functions 
def additive_persistence(n):
 n_str=str(n)
 count=0
 # while length of n_str > 1
 # print("length ",len(n_str))
 while len(n_str) > 1:
  add=0
  # go through string elements
  for i in range(0,len(n_str)):
   # turn to int
   # add to sum
   add+=int(n_str[i])
  count+=1
  n_str=str(add)
 return count
​
def persistence(n):
 n_str=str(n)
 count=0
 while len(n_str) > 1:
  prod=1
  for i in range(0,len(n_str)):
   prod*=int(n_str[i])
  count+=1
  n_str=str(prod)
 return count

