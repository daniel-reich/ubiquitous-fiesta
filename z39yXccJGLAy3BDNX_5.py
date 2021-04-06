
def flipping_bits(n):
  s=bin(n)[2:].zfill(32)
  p=''
  for x in s:
    if x=='0':
      p+='1'
    else:
      p+='0'
  return int(p,2)

