
def camel_to_snake(s):
  converted = ''
  for i in s:
    if i.isupper():
      converted+='_'+i.lower()
    else:
      converted+=i
  return converted

