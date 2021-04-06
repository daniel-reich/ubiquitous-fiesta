
def caesar_cipher(text, key):
  alf = 'abcdefghijklmnopqrstuvwxyz'
  fin = ''
  for a in text:
    if a in alf:
      fin += alf[(alf.index(a)+key)%26]
    else:
      fin += ' '
  return fin

