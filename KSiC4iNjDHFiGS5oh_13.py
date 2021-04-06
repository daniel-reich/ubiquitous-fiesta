
def is_super_d(n):
 # for d = 2 to 9 incl.
 for d in range(2,10):
  # create prod
  prod=d*(n**d)
  # check if prod has d consecutive d's
  count=0
  prod_str=str(prod)
  i=0
  while count < d and i < len(prod_str):
   if int(prod_str[i]) == d:
    count+=1
   else:
    count=0
   i+=1
  # print('count',count)
  # if yes, return d - else "Normal Number" 
  if count == d:
   return "Super-"+str(d)+" Number"
 if count == 0:
  return "Normal Number"

