
def alternating_caps(txt):
  cnter = 0
  out = ""
  for letter in txt:
    if not letter == ' ':
      cnter += 1
    
    if cnter % 2 != 0:
      out += letter.upper()
    else:
      out += letter.lower()
      
  return out

