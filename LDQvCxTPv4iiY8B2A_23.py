
def same_upsidedown(ntxt):
  num = ""
  for dig in ntxt:
    if dig == '6':
      num += '9'
    elif dig == '9':
      num += '6'
    else:
      num += '0'
  return num[::-1] == ntxt

