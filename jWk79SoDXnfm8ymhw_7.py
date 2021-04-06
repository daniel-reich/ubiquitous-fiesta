
def censor(s):
  lst = s.split()
  lst = ["*" * len(word) if len(word) > 4 else word for word in lst]
  return " ".join(lst)

