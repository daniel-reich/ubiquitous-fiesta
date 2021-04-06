
def sigilize(desire):
  s = ''.join([l for l in desire.upper() if l not in 'AEIOU '])
  return ''.join([s[i] for i in range(len(s))  if s[i] not in s[i+1:]])

