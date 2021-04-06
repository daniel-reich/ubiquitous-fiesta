
def atbash(txt):
  s = [chr(155 - ord(i) + 64*i.islower()) if i.isalpha() else i for i in txt ]
  return ''.join(s)

