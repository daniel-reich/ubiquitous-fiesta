
def extend_vowels(word, num):
  new_word = ''
  if num >= 0 and type(num)==int:
    for letter in word:
      new_letter = ''
      if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        for i in range (0, num+1, 1):
          new_letter+=letter
        new_word+=new_letter
      else:
        new_word+=letter
    return new_word
  else:
    return 'invalid'

