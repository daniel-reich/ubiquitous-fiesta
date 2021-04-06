
def tp_checker(home):
  res=int((home['tp']*500)/(home['people']*57))
  if res>=14:
    return 'Your TP will last {} days, no need to panic!'.format(res)
  else:return 'Your TP will only last {} days, buy more!'.format(res)

