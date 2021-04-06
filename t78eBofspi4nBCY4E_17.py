
def base_conv(n,b):
  digits=[chr(ord('a')+i) for i in range(b)]
  if not str(n)[0].isalpha():
    b_str = ''
    if n == 0:
      return '0'
    while n != 0:
      b_str += digits[n % b]
      n = n // b
    return b_str[::-1]
  else:
    b_str = str(n)
    for c in b_str:
      if not c in digits:
        return b_str + ' is not a base ' + str(b) +' number.'
    cumul=0
    for i in range (len(b_str)):
      cumul +=b**(len(b_str)-i-1)*digits.index(b_str[i])
    return cumul

