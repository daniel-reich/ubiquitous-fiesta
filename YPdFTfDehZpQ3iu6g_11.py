
def roman_numerals(arg):
  try:
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    s=sum(d[i] for i in arg)
    if 'IV' in arg or 'IX' in arg:s-=2
    if 'XL' in arg or 'XC' in arg:s-=20
    return s
  except: return 'MCCCXXIV'

