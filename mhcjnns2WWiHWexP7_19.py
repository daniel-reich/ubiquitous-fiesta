
def calculate_arrowhead(lst):
  i = 0
  for elem in lst:
    for sign in elem:
      if sign == ">":
        i += 1
      elif sign == "<":
        i -= 1
  
  if i > 0:
    return ">"*i
  elif i < 0:
    return "<"*(i*-1)
  else:
    return ""

