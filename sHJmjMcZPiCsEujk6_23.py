
pi_digits = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
def pilish_string(txt, digit_idx = 0):
  if len(txt) == 0 or digit_idx >= len(pi_digits):
    return ""
  tarLen = pi_digits[digit_idx]
  if len(txt) >= tarLen:
    temp = pilish_string(txt[tarLen:], digit_idx + 1)
    if len(temp) == 0:
      return txt[:tarLen]
    else:
      return txt[:tarLen] + " " + temp
  else:
    return txt + txt[-1] * (tarLen - len(txt))

