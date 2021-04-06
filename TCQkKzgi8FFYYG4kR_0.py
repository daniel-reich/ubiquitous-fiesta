
def camel_to_snake(s):
  return ''.join('_'+ i.lower() if i == i.upper() and i.isalpha() else i for i in s)

