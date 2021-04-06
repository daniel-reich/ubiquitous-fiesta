
def XO(txt):
  num_of_x = 0
  num_of_o = 0
  for ch in txt.lower():
    if ch == "x":
      num_of_x += 1
    elif ch == "o":
      num_of_o += 1
    
  return num_of_x == num_of_o

