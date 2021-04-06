
def worded_math(equ):
  equ = equ.lower()
  s = equ.split()
  a = 0
  b = 0
  if s[0] == "one":
    a = 1
  elif s[0] == "zero":
    a = 0
  elif s[0] == "two":
    a = 2
  if s[2] == "one":
    b = 1
  elif s[2] == "zero":
    b = 0
  elif s[2] == "two":
    b = 2
  if s[1] == "plus":
    c = a + b
    if c == 0:
      return "Zero"
    elif c == 1:
      return "One"
    elif c == 2:
      return "Two"
  elif s[1] == "minus":
    c = a - b
    if c == 0:
      return "Zero"
    elif c == 1:
      return "One"
    elif c == 2:
      return "Two"

