
def censor(s):
  words = s.split(" ")
  word = ""
  for y,x in enumerate(words):
    if(len(x) > 4):
       for i in x:
          word = word + "*"
       words[y] = word
       word = ""
  return " ".join(words)

