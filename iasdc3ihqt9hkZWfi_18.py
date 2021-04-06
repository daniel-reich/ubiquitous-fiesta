
def can_give_blood(d, r):
  return not(d[-1]=="+" and r[-1]=="-") and (d[0]=="O" or r[:2]=="AB" or (d[0]==r[0] and d[:2]!="AB"))

