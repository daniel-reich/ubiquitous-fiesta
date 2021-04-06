
def tp_checker(home):
  days = int((home.get("tp")*500)/(home.get("people")*57))
  if days < 14:
    return "Your TP will only last " + str(days) + " days, buy more!"
  else:
    return "Your TP will last " + str(days) + " days, no need to panic!"

