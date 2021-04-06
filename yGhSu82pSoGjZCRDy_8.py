
def seesaw(num):
  if num == None or len(str(num)) == 1:
    return "balanced"
  elif len(str(num)) % 2 == 0:
    if int(str(num)[:int(len(str(num))/2)]) > int(str(num)[int(len(str(num))/2):]):
      return "left"
    elif int(str(num)[:int(len(str(num))/2)]) < int(str(num)[int(len(str(num))/2):]):
      return "right"
    else:
      return "balanced"
  elif len(str(num)) % 2 == 1:
    if int(str(num)[:int(((len(str(num)))-1)/2)]) > int(str(num)[int(((len(str(num)))+1)/2):]):
      return "left"
    elif int(str(num)[:int(((len(str(num)))-1)/2)]) < int(str(num)[int(((len(str(num)))+1)/2):]):
      return "right"
    else:
      return "balanced"

