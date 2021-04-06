
def final_direction(initial, turns):
  list1 = ["N","W","S","E","N","W","S","E"]
  index=list1.index(initial)
  no1= turns.count("L")
  no2=turns.count("R")
  no3=no1-no2
  if no3>0:
    return list1[index+no3]
  else:
    return list1[index+no3]

