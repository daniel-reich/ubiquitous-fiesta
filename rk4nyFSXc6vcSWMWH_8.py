
def shared_digits(lst):
 for i in range(0,len(lst)-1):
  output=False
  while output == False: 
   for k in range(0,len(str(lst[i]))):
    if str(lst[i])[k] in str(lst[i+1]):
     output=True
   if output == False:
    return False
 if output != False:
  return True

