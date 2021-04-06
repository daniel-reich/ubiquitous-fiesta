
import numpy as np
def caesar_cipher(s, k):
  new_txt = ""
  letters = [chr(i) for i in range(97, 97+25+1)]
  new = np.roll(np.array(letters), -k)
  d = {letters[i]:new[i] for i in range(len(letters))}
  for i in range(len(s)):
    if s[i].isalpha():
      if s[i].isupper():
        new_txt += d[s[i].lower()].upper()
      else:
        new_txt += d[s[i].lower()]
    else:
      new_txt += s[i]
  return new_txt

