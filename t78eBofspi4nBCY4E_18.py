
def base_conv(n,b):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  if isinstance(n,int):
    s = ''
    while n > 0:
      s += letters[n%b]
      n //= b
    return s[::-1]
  else:
    if any(ch not in letters[:b] for ch in n):
      return '{} is not a base {} number.'.format(n,b)
    m = 0
    for i in range(len(n)):
      m += letters.index(n[i])*b**(len(n)-(i+1))
    return m

