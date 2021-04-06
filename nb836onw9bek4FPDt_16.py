
def count_same_ends(txt):
  c = 0
  txt = txt.lower()
  txt = txt.replace("!", "")
  txt = txt.replace(".", "")
  words = txt.split()
  for word in words:
    if word[0] == word[len(word) - 1] and len(word) != 1:
      c += 1
  return c

