
def extend_vowels(word, num):
  return "".join(x+x*num if x.lower() in 'aeiou' else x for x in word) if type(num) is int and num >= 0 else "invalid"

