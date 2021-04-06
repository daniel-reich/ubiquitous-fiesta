
def extend_vowels(word, num):
  if num < 0 or type(num) is float:
    return "invalid"
  elif num == 0:
    return word
  return "".join(x * (num + 1) if x.lower() in "aeiou" else x for x in word)

