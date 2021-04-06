
def tp_checker(home):
  tp = home["tp"] * 500
  sheetsPerDay = home["people"] * 57
  
  if tp//sheetsPerDay > 14:
    return "Your TP will last {} days, no need to panic!".format(tp//sheetsPerDay)
  return "Your TP will only last {} days, buy more!".format(tp//sheetsPerDay)

