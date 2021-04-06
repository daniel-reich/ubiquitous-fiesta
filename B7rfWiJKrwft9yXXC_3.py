
def sort_decending(num):
  mylist = []
  mystr = ""
  if (0==num):
    return num  
  while (num>0):
    rem = int(num%10)
    num = int(num/10)        
    mylist.append(rem)
  mylist = (sorted(mylist))
  for i in range (len(mylist)):
    mystr = str(mylist[i]) + mystr    
  return int(mystr)

