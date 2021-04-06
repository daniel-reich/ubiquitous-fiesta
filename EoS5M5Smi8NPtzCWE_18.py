
def secret(text):
  a,b = text.split('*')
  a = '<'+a+'>'+'</'+a+'>'
  return a*int(b)

