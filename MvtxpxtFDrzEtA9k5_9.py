
def palindrome_descendant(num):
  num=str(num)
  if len(num)>=2 and (num==num[::-1]):
   return True
  elif len(num)>=2 and len(num)%2==0:
   nwnu=''
   for i in range(0,len(num),2):
     nwnu=nwnu+str(int(num[i])+int(num[i+1]))
   return palindrome_descendant(nwnu)
  return False

