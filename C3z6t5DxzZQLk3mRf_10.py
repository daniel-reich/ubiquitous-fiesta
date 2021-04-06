
import math
def tune(lst):
  print(lst)
  inTune = [329.63, 246.94, 196, 146.83, 110, 82.41]
  result = []
  for i in range(len(lst)):
    t = lst[i]
​
    if t == 0:
      result.append(" - ")
      continue
      
    dif =  inTune[i] - t
    
    above = dif < 0
    perc = (dif/inTune[i])*100
    intPerc = abs(round(perc))
    print(intPerc)
    if ( intPerc >= 1 and intPerc <= 2 ):
      if (above):
        result.append("+<")
      else:
        result.append(">+")
    elif (intPerc >= 3):
      if (above):
          result.append("+<<")
      else:
        result.append(">>+")
    else:
      result.append("OK")
  return result

