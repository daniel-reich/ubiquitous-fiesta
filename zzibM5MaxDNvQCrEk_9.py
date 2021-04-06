
def will_fit(holds, cargo):
  for i in range(0,len(holds)):
    if holds[i] == "S" and cargo[i]>50:
      return False
    elif holds[i] == "M" and cargo[i]>100:
      return False
    elif holds[i] == "L" and cargo[i]>200:
      return False
  return True

