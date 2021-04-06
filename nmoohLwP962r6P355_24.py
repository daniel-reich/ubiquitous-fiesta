
def straight_digital(number):
  st = str(number)
  le = len(st)
  if le<3 or number<0: return 'Not Straight'
  
  stL = st[:-1]
  stR = st[1:]
  difLst = [int(chR) - int(chL) for chL, chR in zip(stL, stR)]
  dif = difLst[0]
  
  if difLst != [dif] * (le-1): return 'Not Straight'
  if dif == 0: return 'Trivial Straight'
  else: return dif

