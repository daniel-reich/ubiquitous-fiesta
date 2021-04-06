
def sigilize(desire):
  a = ''.join(desire.upper().split())
  b = sorted(set(a), key=a.rindex)
  return ''.join(i for i in b if i not in "AEIOU")

