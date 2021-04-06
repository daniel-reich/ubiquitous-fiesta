
symbols  = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
​
def digitToRN(dig, place):
  if dig < 4:
    return symbols[place] * dig
  elif dig == 4:
    return symbols[place] + symbols[place * 5]
  elif dig < 9:
    return symbols[place * 5] + symbols[place] * (dig - 5)
  else:
    return symbols[place] + symbols[place * 10] 
    
def convert_to_roman(num):
  parts, pv  = [], 1
  while num:
    digit = num % 10
    num = num // 10
    parts.append(digitToRN(digit, pv))
    pv *= 10
  return ''.join(reversed(parts))

