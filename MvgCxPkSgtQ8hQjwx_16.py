
def remove_vowels(words):
  new_words = ""
  vowels = "aAeEiIoOuU"
  for i in words:
    add_cond = True
    for x in vowels:
      if i == x:
        add_cond = False
    if add_cond:
      new_words += i
  return new_words

