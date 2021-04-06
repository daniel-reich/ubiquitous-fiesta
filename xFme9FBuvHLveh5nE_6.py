
def is_zygodrome(num):
  word = str(num)
  counter = 1
  for i, v in enumerate(word):
    if i != len(word) - 1:
      if counter == 1 and v != word[i+1]:
        return False
      elif v == word[i+1]:
        counter += 1
      else:
        counter = 1
    elif counter == 1:
      return False
    else:
      return True

