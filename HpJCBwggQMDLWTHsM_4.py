
def average_word_length(txt):
  a = 0
  for letter in txt:
    if not letter in ",. !?":
      a += 1
  return round((a / (txt.count(" ") + 1)),2)

