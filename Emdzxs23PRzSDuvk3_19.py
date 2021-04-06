
def pizza_points(customers, min_orders, min_price):
  new_lst=[]
  for i in customers:
    total=0
    for j in customers[i]:
      if j>=min_price: total+=1
    if total>=min_orders: new_lst.append(i)
  return sorted(new_lst)

