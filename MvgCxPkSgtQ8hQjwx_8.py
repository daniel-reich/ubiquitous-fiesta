
def remove_vowels(txt):
  table = txt.maketrans(dict.fromkeys('AEIOUaeiou'))
  return txt.translate(table)

