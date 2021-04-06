
def special_reverse(s, c):
  return " ".join(word if word[0] != c else word[::-1] for word in s.split())

