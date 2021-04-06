
def lemonade(bills):
  five = bills.count(5)
  ten = bills.count(10)
  for i in bills:
    if i ==10:
      five-=1
    if i == 20:
      if ten >0:
        ten-=1
        five-=1
      else :
        five -=3
  return five>=0 and ten>=0

