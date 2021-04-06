
def worded_math(equ):
  d={"ZERO":0,"ONE":1,"TWO":2}
  eq=equ.upper().split()
  if eq[1]=="PLUS":
    return (list(d.keys())[list(d.values()).index(d[eq[0]]+d[eq[2]])]).capitalize() 
  return (list(d.keys())[list(d.values()).index(d[eq[0]]-d[eq[2]])]).capitalize()

