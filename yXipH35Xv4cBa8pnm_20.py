
def microwave_buttons(time):
  res = 1
  parts = time.split(":")
  if int(parts[0]) == 1 and int(parts[1]) == 0:
    res += 2
  elif int(parts[1]) % 30 == 0 and int(parts[1]) > 0:
    res += int(parts[1]) / 30
  else:
    idx = time.index(':')
    for i in range(0,len(time)):
      if time[i] != ':' and time[i] != '0':
        if i < idx:
          return res + len(time) - i - 1
        else:
          return res + len(time) - i
  return res

