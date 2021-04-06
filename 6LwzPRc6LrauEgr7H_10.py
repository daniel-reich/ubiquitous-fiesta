
def worm_length(worm):
  
  total = 0
  if (worm.count("-") == len(worm)) and (worm != ""):
    for item in list(worm):
      total += 10
  
  else:
    return "invalid"
​
  return "{} mm.".format(str(total))

