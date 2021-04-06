
def anagram(name, words):
  x = "".join(sorted(name.lower())) 
  word_string = ""
  for i in words:
    word_string += i
  y = "".join(sorted(word_string.lower()))
  return y == x.strip()

