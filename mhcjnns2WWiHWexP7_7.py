
def calculate_arrowhead(lst):
  pos=0
  for st in lst:
    if st[0]=="<":
      pos-=len(st)
    elif st[0]==">":
      pos+= len(st)
  if pos<0:
    return "<"*(-1*pos)
  elif pos>0:
    return ">"*pos
  else : return ""

