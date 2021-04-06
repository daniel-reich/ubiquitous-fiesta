
def validate_relationships(txt):
  exp = ''
  for char in txt:
    if char == '=' and exp[-1] not in '<>':
      exp += '=='
    else:
      exp += char
  return eval(exp)

