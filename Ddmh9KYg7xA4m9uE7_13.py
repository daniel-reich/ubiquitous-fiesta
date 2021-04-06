
def convert_binary(s):
  s = list(s.lower())
  lst = []
  for l in s:
    if ord(l) in range(97, 110):
      lst.append('0')
    elif ord(l) in range(109, 123):
      lst.append('1')
  return ''.join(lst)

