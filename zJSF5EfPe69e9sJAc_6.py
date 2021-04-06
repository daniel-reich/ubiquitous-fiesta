
def censor_string(txt, lst, char):
  words = txt.split(" ")
  for i, word in enumerate(words):
    if word in lst:
      words[i] = "".join([char for letter in word])
  return " ".join(words)

