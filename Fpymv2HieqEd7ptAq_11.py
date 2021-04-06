
def split(txt):
  result = []
  open_count = 0
  closed_count = 0
  
  subset = ""
  
  for char in txt:
    if char == "(":
      subset += "("
      open_count += 1
    if char == ")":
      subset += ")"
      closed_count += 1
      if closed_count == open_count:
        result.append(subset)
        subset = ""
  
  return result

