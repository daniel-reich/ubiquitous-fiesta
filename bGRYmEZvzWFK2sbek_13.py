
def get_missing_letters(s):
  import string
  slist = list(s)
  f = ""
  for letter in string.ascii_lowercase:
    if letter not in slist:
      f += letter
  return f

