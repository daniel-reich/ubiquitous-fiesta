
def is_alpha(word):
  return not sum([ord(i)-96 for i in word if i.isalpha()]) % 2

