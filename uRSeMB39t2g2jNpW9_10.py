
def turn_calc(num):
  dic = dict(zip('123456780','IZEHSGLBO'))
  return ''.join(dic[c] for c in str(num).replace('.','')[::-1] if c in dic)

