
def dashed(txt):
  vowels  = ['a','e','i','o','u','A','E','I','O','U']
  lista = ['-{}-'.format(i)if i in vowels else i for i in txt ]
  return ''.join(lista)

