
def seesaw(num):
  num = str(num)
  if len(num) < 2:
    return 'balanced'
  fulcrum = len(str(num)) // 2
  try:
    if int(num[:fulcrum]) > int(num[-fulcrum:]):
      return 'left'
    if int(num[:fulcrum]) < int(num[-fulcrum:]):
      return 'right'
  except:
    return 'balanced'
  return 'balanced'

