
def is_palindrome_possible(txt):
  freqs = {i:txt.count(i)%2 for i in txt}
  return list(freqs.values()).count(1) <= 1

