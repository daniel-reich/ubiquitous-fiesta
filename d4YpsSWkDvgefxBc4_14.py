
def over_twenty_one(cards):
  pnts=0
  for x in cards:
    if isinstance(x,int)==True: pnts = pnts+x
    elif x == "A": continue
    else: pnts = pnts + 10  
  if "A" in cards:
    if pnts == 20: pnts = pnts + 1
    else: pnts = pnts + 11
  return pnts > 21

