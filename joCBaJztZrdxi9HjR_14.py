
def tp_checker(home):
  a = home["people"] * 57
  b = home["tp"] * 500
  d = b // a
​
  if d < 7:
    return "Your TP will only last {0} days, buy more!".format(d)
  elif d > 7 and d < 14:
    return "Your TP will only last {0} days, buy more!".format(d)
  else : return "Your TP will last {0} days, no need to panic!".format(d)

