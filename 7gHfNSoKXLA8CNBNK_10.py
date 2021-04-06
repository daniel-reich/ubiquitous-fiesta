
def divisible(n):
  lst=[]
  for i in range (2,n):
    if (n%i==0):
      lst.append(i)
  return lst
​
def sim_prop_frac(max_den):
  result=0
  for i in range (1,max_den+1):
    for j in range (1,max_den+1):
      if (i/j < 1 and (j%i >0 or i==1) and len([c for c in divisible(i) if c in divisible(j)])==0):
        result+=1
  return result

