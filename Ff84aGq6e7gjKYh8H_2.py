
def minutes_to_seconds(time):
  converted=time.split(":")
  if int(converted[1])>=60:
    return False
  else:
    a=int(converted[0])*60
    b=int(converted[1])
    return a+b

