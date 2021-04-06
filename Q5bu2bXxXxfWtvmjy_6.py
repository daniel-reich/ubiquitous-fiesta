
def missing_letter(txt):
  k = []
  for letter in txt:
    k.append(ord(letter)) 
  for index in range(min(k),max(k)):
    if k.count(index) == 0:
      return chr(index)
  return "No Missing Letter"

