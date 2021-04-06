
def tp_checker(dic):
  D = dic['tp']*500 // (dic['people']*57)
  if D<14: return 'Your TP will only last {} days, {}!'.format(D, 'buy more')
  return "Your TP will last {} days, {}!".format(D,"no need to panic")

