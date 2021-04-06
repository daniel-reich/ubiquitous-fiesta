
def secret(text):
  n = int(text[-1])
  a = '<' + text[:-2] + '>'
  b = '</' + text[:-2] + '>'
  c = a+b
  return n*c

