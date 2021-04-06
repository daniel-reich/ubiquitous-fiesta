
def camel_to_snake(s):
  for char in s:
    if str.isupper(char):
      s = s.replace(char, '_' + str.lower(char))
  return s

