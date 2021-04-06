
def validate_relationships(txt):
  ready = ''
  for i in range(len(txt)):
    if txt[i] == '=':
      if txt[i-1] not in ('<','>'):
        ready += '=='
      else:
        ready += txt[i]
    else:
      ready += txt[i]
  return eval(ready)

