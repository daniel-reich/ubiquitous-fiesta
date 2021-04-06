
def parse_roman_numeral(num):
  d=0
  rns = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,
  "XC":90,"L":50,"XL":40,"X":10,"V":5,"IV":4,"I":1}
  for i in range(len(num)):
    d+=rns[num[i]]
  if 'IX' in num or 'IV' in num:
    d = d-2
  if 'CD' in num or 'CM' in num:
    d = d-200
  if 'XL' in num or 'XC' in num: 
    d = d-20
  return d

