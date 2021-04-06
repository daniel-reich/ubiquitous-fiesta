
def worded_math(equ):
  c = []
  for i in equ.split():
    i = i.lower()
    if i == "one":
      c.append("1")
    elif i == "zero":
      c.append("0")
    elif i=="plus":
      c.append("+")
    elif i=="minus":
      c.append("-")
  
  if eval("".join(c)) == 2:
    return "Two"
  elif eval("".join(c)) == 1:
    return "One"
  elif eval("".join(c)) == 0:
    return "Zero"

