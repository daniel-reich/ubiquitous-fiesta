
import math
def tp_checker(home):
  need = home["people"] * 14 * 57
  have = home["tp"] * 500
  days = math.floor(have/(need/14))
  if have >= need:
    return "Your TP will last " + str(days) +" days, no need to panic!"
  else:
    return "Your TP will only last " + str(days) +" days, buy more!"

