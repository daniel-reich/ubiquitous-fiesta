
def turn_calc(num):
  t=[int(x) for x in str(num) if x.isdigit()]
  s='OIZEHSGLB-'
  r=''
  for x in t:
    r+=s[x]
  return r[::-1]

