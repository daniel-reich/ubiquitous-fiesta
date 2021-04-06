
def to_list(num):
  mylist = []
  str_num = str(num)
  for i in range (len(str_num)):
    mylist.append(int(str_num[i]))
  return mylist
  
def to_number(lst):
  mul = 0
  for i in range (len(lst)):
      mul = mul*10 + lst[i]
  return mul

