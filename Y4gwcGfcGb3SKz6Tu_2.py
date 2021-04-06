
import re
def max_separator(txt):
  al = 'abcdefghijklmnopqrstuvwxyz'
  M = max(max([0]+[len(m) for m in re.findall('{}[^{}]*(?={})'.format(l,l,l),txt)]) for l in al)
  if M==0: return []
  return [l for l in al if max([0]+[len(m) for m in re.findall('{}[^{}]*(?={})'.format(l,l,l),txt)])==M]

