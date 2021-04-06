
def camel_to_snake(s):
  words = s.split(' ')
  newtxt = ''
  for word in words:
    for char in word:
      if char.isupper():
        newtxt += '_' + char.lower()
      else:
        newtxt += char
    newtxt += ' '
  return newtxt[:-1]

