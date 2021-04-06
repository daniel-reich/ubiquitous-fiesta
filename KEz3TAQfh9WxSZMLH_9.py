
import string
def count_all(txt):
  lettcount = 0
  digicount = 0
  
  for i in txt:
    if i in string.ascii_lowercase or i in string.ascii_uppercase:
      lettcount += 1
    elif i in "0123456789":
      digicount += 1
      
  
  return {'LETTERS':lettcount,'DIGITS':digicount}

