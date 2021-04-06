
def small_favor(sentence):
  s = sentence.split()
  for i in range(len(s)):
    if s[i].count('.')==2:
      temp = s[i].split('.')
      if int(temp[2])>20:
        temp[2] = '19'+temp[2]
      else:
        temp[2] = '20'+temp[2]
      s[i] = '.'.join(temp)
    elif s[i].count('/')==2:
      temp = s[i].split('/')
      if int(temp[2])>20:
        temp[2] = '19'+temp[2]
      else:
        temp[2] = '20'+temp[2]
      s[i] = '/'.join(temp)
    elif s[i] in ['January,','February,','March,','April,','May,','June,','July,','August,','September,','October,','November,','December,']:
      if int(s[i+2][:-1])>20:
        s[i+2] = '19'+s[i+2]
      else:
        s[i+2] = '20'+s[i+2]
  return ' '.join(s)

