
def minutes_to_seconds(time):
  return False if int(time.split(":")[1])>=60 else int(time.split(":")[0])*60+int(time.split(":")[1])

