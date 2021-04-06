
def count_all(txt):
  letter_counter = 0
  number_counter = 0
  for i in txt:
    if i.isalpha():
      letter_counter += 1
    elif i in '0123456789':
      number_counter += 1
  return {'DIGITS': number_counter, 'LETTERS': letter_counter}

