
def time_to_eat(current_time):
  split = current_time.index(":")
  hour = int(current_time[:split])
  if current_time[-4::] == "p.m.":
    hour += 12
  mins = int(current_time[split+1:split+3])
  if hour < 7:
    hoursuntil = 6 - hour
    minsuntil = 60 - mins
  elif hour < 12:
    hoursuntil = 11 - hour
    minsuntil = 60 - mins
  elif hour < 19:
    hoursuntil = 18 - hour
    minsuntil = 60 - mins
  else:
    hoursuntil = 30 - hour
    minsuntil = 60 - mins
  if minsuntil == 60:
    minsuntil = 0
    hoursuntil += 1
  return [hoursuntil, minsuntil]

