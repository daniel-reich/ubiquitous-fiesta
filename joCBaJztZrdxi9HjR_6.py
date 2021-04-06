
def tp_checker(home):
  sheets_per_day = home["people"] * 57
  total_sheets = home["tp"] * 500
  days = total_sheets // sheets_per_day
  if days < 14:
    return "Your TP will only last {} days, buy more!".format(days)
  else:
    return "Your TP will last {} days, no need to panic!".format(days)

