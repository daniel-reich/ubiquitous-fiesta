
def tp_checker(home):
  x = int((home['tp'] * 500) / (home['people'] * 57))
  if x < 14:
    return "Your TP will only last " + str(x) +" days, buy more!"
  return "Your TP will last " + str(x) + " days, no need to panic!"

