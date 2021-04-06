
def minutes_to_seconds(time):
  time_list = time.split(":")
  if float(time_list[1]) >=60:
    return False 
  else:
    minutes = float(time_list[0])*60 + float(time_list[1])
    return minutes

