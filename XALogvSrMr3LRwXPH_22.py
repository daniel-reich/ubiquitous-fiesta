
def is_shuffled_well(lst):
  num=0
  num1=0
  for i in lst:
   if num==2:
    return False
   if num1+1==i or num1-1==i:
    num=num+1
   else:
    num=0
   num1=i
  return True

