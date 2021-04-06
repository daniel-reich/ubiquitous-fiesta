
def no_strangers(txt):
  acq = []
  fr = []
  total = {}
  txt = txt.replace(".", "")
  txt = txt.replace(",", "")
  txt = txt.replace("\"", "")
  txt = txt.lower()
  words = txt.split(" ")
  for word in words:
    if (word in total):
      total[word] += 1
      if (total[word] == 3):
        acq.append(word)
      if (total[word] == 5):
        fr.append(word)
        acq.remove(word)
    else:
      total[word] = 1
  return [acq, fr]

