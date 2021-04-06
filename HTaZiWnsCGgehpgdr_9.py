
def license_plate(s, n):
  s = ''.join([i.upper() for i in s if i!='-'])[::-1]
  return '-'.join([s[i:i+n][::-1] for i in range(0,len(s),n)][::-1])

