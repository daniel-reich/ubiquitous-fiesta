
def num_of_days(cost, savings, start):
  money = savings
  day = 0
  val = start
  while money<cost:
    money += val
    day += 1
    val+=1
    if day%7==0:
      val-=6
  
  return day

