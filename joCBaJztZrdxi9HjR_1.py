
def tp_checker(q):
  d = (q['tp']*500)//(q['people']*57)
  return ['Your TP will last {} days, no need to panic!'.format(d),
    'Your TP will only last {} days, buy more!'.format(d)][d < 14]

