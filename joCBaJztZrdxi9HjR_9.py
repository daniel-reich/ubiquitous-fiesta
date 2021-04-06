
def tp_checker(home):
  d = int(home['tp']/home['people']/.114)
  return ('Your TP will last %d days, no need to panic!',
      'Your TP will only last %d days, buy more!')[d < 14] % d

