
def order_people(lst, people):
  if lst[0]*lst[1]<people:
    return "overcrowded"
  count=1
  arr=[]
  for i in range(lst[0]):
    temp=[]
    for j in range(lst[1]):
      if count<=people:
        temp.append(count)
      else:
        temp.append(0)
      count+=1
    if i%2==1:
      temp.reverse()
      arr.append(temp)
    else:
      arr.append(temp)
  return arr

