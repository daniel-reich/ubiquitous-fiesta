
def no_duplicate_letters(phrase):
  switch = True
  spliter = phrase.lower().split()
  for word in spliter:
    for letter in word:
      if word.count(letter) > 1:
        switch = False
  return switch

