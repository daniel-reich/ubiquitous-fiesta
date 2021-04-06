
def camel_to_snake(s):
  return ' '.join([c2s(i) for i in s.split()])
  
def c2s(s):
  return ''.join([i if not i.isalpha() or i.islower() else '_'+i.lower() for i in s])

