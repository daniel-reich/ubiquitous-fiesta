
def bill_split(spicy, cost):
  my_pay=0
  friend_pay=0
  i=0
  total_cost=[]
  while i<len(spicy):
    if spicy[i]=='S':
      my_pay+=cost[i]
      i+=1
    else:
      my_pay+=cost[i]/2
      friend_pay+=cost[i]/2
      i+=1
  
  total_cost.append(my_pay)
  total_cost.append(friend_pay)
  return total_cost

