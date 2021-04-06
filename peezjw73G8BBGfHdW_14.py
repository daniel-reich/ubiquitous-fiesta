
def arithmetic_operation(n):
  
  Text = str(n)
  
  Blocks = Text.split(" ")
  
  if (Blocks[1] == "//") and (Blocks[2] == "0"):
    return -1
  
  elif (Blocks[1] == "+"):
    return int(Blocks[0]) + int(Blocks[2])
  
  elif (Blocks[1] == "-"):
    return int(Blocks[0]) - int(Blocks[2])
  
  elif (Blocks[1] == "*"):
    return int(Blocks[0]) * int(Blocks[2])
  
  elif (Blocks[1] == "//"):
    return int(Blocks[0]) // int(Blocks[2])
  
  else:
    return "I don't know"

