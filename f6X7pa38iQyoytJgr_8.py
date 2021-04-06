
def increasing_word_weights(sentence):
  words = sentence.split()
  current = 0
  for word in words:
    total = 0
    for char in word:
      if char.isalpha():
        total += ord(char)
    if total <= current:
      return False
    else:
      current = total
  return True

