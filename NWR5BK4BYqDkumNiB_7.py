
def digital_division(n):
  each = all(n%int(x) == 0 for x in str(n) if x!='0' )
  s = n% sum(int(x) for x in str(n)) == 0
  pr = n% eval('*'.join(x for x in str(n))) == 0 if '0' not in str(n) else 0
  rez = each + s + pr 
  return "Perfect" if rez == 3  else rez if rez else "Indivisible"

