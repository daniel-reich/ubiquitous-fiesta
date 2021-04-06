
import string
def replace(txt, r):
  letters = string.ascii_lowercase
  start_index = letters.find(r[0])
  end_index = letters.find(r[2])
  to_hash = letters[start_index:end_index+1]
  for letter in txt:
    if letter in to_hash:
      txt = txt.replace(letter,'#')
  return txt

