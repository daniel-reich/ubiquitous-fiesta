
def rotated_words(txt):
  
  valid_chars = ["H", "I", "N", "O", "S", "X", "Z", 'M', 'W']
  
  words = list(set(txt.split()))
  c = 0
  
  for word in words:
    word_valid = True
    for char in word:
      if char not in valid_chars:
        word_valid = False
        break
    if word_valid == True:
      c += 1
  
  return c

