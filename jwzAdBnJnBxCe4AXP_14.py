
def rearranged_difference(a):
 s,d='',''
 for i in str(sorted([int(i) for i in str(a)])):
  if i.isdigit()==True:
   s+= i
 for i in str(sorted([int(i) for i in str(a)],reverse=True)):
  if i.isdigit()==True:
   d+= i
 return float(d)-float(s)

