
def formula(txt):
  a = 4
  if len(txt) == 0:
    return None
  
  parts = txt.split()
  values = []
  current = 0
  equ = 0
  symbol = ""
  for part in parts:
    if part == "a":
      current = 4
      
    if part.isnumeric():
      current = int(part)
    if part.isnumeric() or part == "a":
      if symbol == "*":
        equ *= current
      elif symbol == "/":
        equ = equ / current
      elif symbol == "-":
        equ -= current
      elif symbol == "+":
        equ += current
      else:
        equ = current
    else:
      if part == "=":
        values.append(equ)
        symbol = ""
        current = 0
      else:
        symbol = part
  
  values.append(equ)
  previous = -1
  for val in values:
    if previous != val and previous != -1:
      return False
    previous = val
  
  return True

