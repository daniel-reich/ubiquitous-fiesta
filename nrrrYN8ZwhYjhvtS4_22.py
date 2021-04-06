
def extend_vowels(word, num):
  if not isinstance(num, type(1)) or num < 0:
    return 'invalid'
  res = ""
  for char in word:
    if char.lower() in "aeiouy":
      res += char*(num+1)
    else:
      res += char
  return res

