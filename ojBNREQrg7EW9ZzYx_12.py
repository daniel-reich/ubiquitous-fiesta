
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
  try:
    x=int([i.replace('$','') for i in total_money.split() if i.replace('$','').isnumeric()][0])
    y=int([i.replace('$','') for i in cost_of_one_chocolate.split() if i.replace('$','').isnumeric()][0])
    eatable_chocolate=x//y
    wrappers=eatable_chocolate
    while not wrappers<=2:
      m=wrappers//3
      eatable_chocolate+=m
      wrappers=wrappers%3
      wrappers+=m
    return eatable_chocolate
  except:
    return 'Invalid Input'

