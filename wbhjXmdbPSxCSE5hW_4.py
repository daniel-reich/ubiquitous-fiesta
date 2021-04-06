
def sigilize(txt):
  return ''.join(i for i in sorted(set(txt[::-1]), key=txt[::-1].index) if i not in 'AEIOUaeiou ')[::-1].upper()

