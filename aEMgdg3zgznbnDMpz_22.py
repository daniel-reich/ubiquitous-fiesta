
def rotated_words(txt: str) -> int:
  rotators = set('HIMNOSWXZ')
  result = 0
  for word in set(txt.split(' ')):
    if len(word) > 0 and all(letter in rotators for letter in word):
      result += 1
  return result

