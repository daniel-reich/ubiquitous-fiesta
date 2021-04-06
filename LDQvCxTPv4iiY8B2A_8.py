
def same_upsidedown(ntxt):
  res = ntxt.replace('6', '%temp%').replace('9', '6').replace('%temp%', '9')
  return res[::-1]==ntxt

