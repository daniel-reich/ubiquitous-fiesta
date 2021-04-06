
def tp_checker(home):
  people = home['people']
  tp = home['tp']
  day = int(tp*500/(people*57))
  if day >=14:
    return "Your TP will last "+ str(day)+" days, no need to panic!"
  else:
    return "Your TP will only last " +str(day)+ " days, buy more!"

