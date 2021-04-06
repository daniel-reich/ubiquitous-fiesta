
def num_of_days(cost, savings, start):
  days = 0
  while(savings<cost):
    for i in range(7):
      days+=1
      savings+=start+i
      if savings>+cost: break
    start+=1
  return days

