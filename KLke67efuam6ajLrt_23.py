
def shuffle_count(num):
  lst = []
  num2 = int(num/2)
  for i in range(num):
      lst.append(i+1)
  newlst = []
  newlst.append(lst[:])
  newrow = []
  count = 1
  for j in range(num2):
      newrow.append(lst[j])
      newrow.append(lst[num2+j])
  newlst.append(newrow)
  while newrow != lst:
      newrow = []
      for k in range(num2):
          newrow.append(newlst[count][k])
          newrow.append(newlst[count][num2+k])
      count = count + 1
      newlst.append(newrow)
  return count

