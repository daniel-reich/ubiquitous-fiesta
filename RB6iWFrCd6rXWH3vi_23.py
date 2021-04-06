
def longest_substring(digits):
  ret = ''
  tmp = str(digits[0])
  odd = True
  if int(digits[0])%2 == 0: odd = False
  for i in range(1,len(digits)):
    if odd and int(digits[i])%2==0:
      tmp+=str(digits[i])
      odd = False
    elif not odd and int(digits[i])%2!=0:
      tmp+=str(digits[i])
      odd = True
    else:
      if len(tmp) > len(ret):
        ret = tmp
      tmp=str(digits[i])
      if int(digits[i])%2 != 0: odd = True
      else: odd = False
  if len(tmp) > len(ret): ret = tmp
  return ret

