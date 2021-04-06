
def tp_checker(home):
  d=home['tp']*500//(home['people']*57)
  return'Your TP will '+('last %s days, no need to panic!'if d>14else'only last %s days, buy more!')%d

