
def return_end_of_number(num):
  num = str(num)
  if num.endswith('0') or num.endswith('4') or num.endswith('5') or num.endswith('6') or num.endswith('7') or num.endswith('8') or num.endswith('9'):
    return num + '-TH'
  else:
    if num.endswith('1'):
      if num.endswith('11'):
        return num + '-TH'
      return num+'-ST'
    if num.endswith('2'):
      if num.endswith('12'):
        return num + '-TH'
      return num+'-ND'
    if num.endswith('13'):
      return num+'-TH'
    return num+'-RD'

