
def tp_checker(home):
  spd = home['people'] * 57
  squares = home['tp'] * 500
  days = squares//spd
  if days < 14:
    return "Your TP will only last " + str(days) + " days, buy more!"
  return "Your TP will last " + str(days) + " days, no need to panic!"

