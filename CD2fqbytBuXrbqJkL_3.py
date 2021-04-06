
def can_build(txt1, txt2):
  txt1 = txt1.replace(' ', '')
  txt2 = txt2.replace(' ', '')
  for letter in txt1:
    if txt1.count(letter) > txt2.count(letter):
      return False
  return True

