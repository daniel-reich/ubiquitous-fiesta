
def license_plate(s, n):
  s = s.replace('-','')[::-1].upper()
  return '-'.join(s[i:i+n] for i in range(0,len(s),n))[::-1]

