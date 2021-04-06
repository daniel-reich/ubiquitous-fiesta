
def extend_vowels(word, num):
  vols = 'aeiouAEIOU'
  new = ''
  if num < 0 or type(num) == float:
    return 'invalid'
  elif num == 0:
    return word
  else:
    for char in word:
      if char not in vols:
        new = new + char
      else:
        new = new + char + (char * num)
    return new

