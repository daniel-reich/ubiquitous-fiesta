
def tune(lst):
  print(lst)
  freqs = [329.63, 246.94, 196.00, 146.83, 110.00, 82.41]
  result = []
  
  for i in range(len(lst)):
    if lst[i] == 0:
      result.append(" - ")
    else:
      error = (lst[i]-freqs[i])/freqs[i]
      error = round(error, 2)
      if error >= 0.01:
        if error >= 0.03:
          result.append("+<<")
        else:
          result.append("+<")
      elif error <= -0.01:
        if error <= -0.03:
          result.append(">>+")
        else:
          result.append(">+")
      else:
        result.append("OK")
      
  return result

