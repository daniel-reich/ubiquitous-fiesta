
def average_word_length(txt):
  arr = []
  txt = txt.replace(",","")
  txt = txt.replace(".","")
  txt = txt.replace("?","")
  txt = txt.replace("!","")
  for w in txt.split():
    arr.append(len(w))
  return round(sum(arr) / len(arr),2)

