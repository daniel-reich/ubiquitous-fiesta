
def make_title(s):
  lst = [word[0].upper() + word[1:] for word in s.split()]
  return " ".join(lst)

