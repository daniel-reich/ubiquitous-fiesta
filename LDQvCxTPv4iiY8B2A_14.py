
def same_upsidedown(ntxt):
  digits = []
  for i in ntxt:
    if i == '6':
      digits.append('9')
    elif i == '9':
      digits.append('6')
    else:
      digits.append(i)
  return ntxt[::-1] == ''.join(digits)

