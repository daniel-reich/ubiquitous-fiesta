
def tp_checker(home):
  days = home["tp"]*500 // (home["people"]*57)
  if days < 14:
    return "Your TP will only last {} days, buy more!".format(days)
  return "Your TP will last {} days, no need to panic!".format(days)

