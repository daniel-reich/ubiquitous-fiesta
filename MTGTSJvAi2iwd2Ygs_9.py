
def valid_division(d):
  
  Text = str(d)
  Blocks = Text.split("/")
  
  Top = int(Blocks[0])
  Bottom = int(Blocks[1])
  
  if (Bottom == 0):
    return "invalid"
  elif (Top % Bottom == 0):
    return True
  else:
    return False

