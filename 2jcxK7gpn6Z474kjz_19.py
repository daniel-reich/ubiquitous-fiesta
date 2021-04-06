
def security(txt):
  alarm = False
  casino = list(txt)
  while "x" in casino:
    casino.remove("x")
  for i in range(len(casino)):
    if casino[i] == "$":
      if i == 0:
        if casino[1] == "T":
          alarm = True
      elif i == len(casino) - 1:
        if casino[-2] == "T":
          alarm = True
      else:
        if casino[i - 1] == "T" or casino[i + 1] == "T":
          alarm = True
  if alarm:
    return "ALARM!"
  else:
    return "Safe"

