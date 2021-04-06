
def check_title(txt):
  return all(ord(word[0]) <= 90 for word in txt.split())

