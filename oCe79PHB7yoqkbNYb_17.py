
def break_point(num):
  list1=[]
  for i in range(len(str(num))):
    list1.append(int(str(num)[i]))
  for i in range(len(list1)):
    if sum(list1[:i])==sum(list1[i:]):
      return True
  return False

