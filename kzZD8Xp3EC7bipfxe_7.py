
def worded_math(equ):
  equ = equ.lower()
  for a, b in [["zero", "0"], ["one", "1"], ["plus", "+"], ["minus", "-"]]:
    equ = equ.replace(a, b)
    
  return ["Zero", "One", "Two"][eval(equ)]

