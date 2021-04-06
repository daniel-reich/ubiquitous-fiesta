
import string
​
def paul_cipher(txt):
  txt = txt.lower()
  first_letter_count = 0
  previous_letter = ''
  emptystring = ''
  lower_alphabet = " " + string.ascii_lowercase
  for i in range(len(txt)):
    if txt[i] in lower_alphabet and txt[i] != ' ':
      if first_letter_count == 0:
        previous_letter = txt[i]
        first_letter_count += 1
        emptystring += previous_letter.upper()
      else:
        current_letter = txt[i]
        shift_index = lower_alphabet.index(previous_letter)
        current_index = lower_alphabet.index(current_letter)
        res_index = shift_index + current_index
        while res_index > 26:
          res_index -= 26
        res_letter = lower_alphabet[res_index]
        emptystring += res_letter.upper()
        previous_letter = txt[i]
    else:
      emptystring += txt[i]
  return emptystring

