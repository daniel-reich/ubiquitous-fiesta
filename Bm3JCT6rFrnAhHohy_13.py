
def alphabet_index(txt):
  result=''
  for character in txt:
    if character.isalpha():
      if character.isupper():
        result+=str(ord(character)-64)+' '
      else:
        result+=str(ord(character)-96)+' '
  return result[:-1]

