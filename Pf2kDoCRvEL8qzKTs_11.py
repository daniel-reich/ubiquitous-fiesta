
def order_people(lst, people):
  # return people
  lst2, lst3, j = [], [], 0
  if(lst[0]*lst[1] < people):
    return "overcrowded"
  else:
    for i in range(1,(lst[0]*lst[1])+1):
      if(i%lst[1]==0):
        lst2.append(0) if i>people else lst2.append(i)
        if(j==0):
          j = 1
          lst3.append(lst2)
        else:
          j = 0
          lst2.reverse()
          lst3.append(lst2)
        lst2 = []
      else:
        lst2.append(0) if i>people else lst2.append(i)
​
    return lst3

