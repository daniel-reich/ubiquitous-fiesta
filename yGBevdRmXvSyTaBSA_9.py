
def sort_drinks_by_price(drinks):
  res =[drinks[0]]
  for idx in range(1,len(drinks)):
    i = 0
    while True:
      if drinks[idx]['price'] < res[i]['price']:
        res.insert(i, drinks[idx])
        break
      else: 
        i += 1
        if i == len(res):
          res.insert(i, drinks[idx])
          break
  return res

