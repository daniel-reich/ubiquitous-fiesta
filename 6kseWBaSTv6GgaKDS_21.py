
def next_letters(s):
  res, r = '', True
  for i in s[::-1]:
    if r:
      res += [chr(ord(i)+1), 'A'][i == 'Z']
      r = i == 'Z'
    else:
      res += i
  return '{}{}'.format('A' * r, res[::-1])

