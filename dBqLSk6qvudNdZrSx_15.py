
def is_boiling(temp):
  if "C" in temp:
    temp=temp[:-1]
    temp=int(temp)
    if temp>=100:
      return(True)
    else:
      return(False)
  if "F" in temp:
    temp=temp[:-1]
    temp=int(temp)
    if temp>=212:
      return(True)
    else:
      return(False)

