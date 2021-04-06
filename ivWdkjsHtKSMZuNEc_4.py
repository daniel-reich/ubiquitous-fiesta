
def find_shortest_words(txt):
  txt = txt.split(" ")
  shortest_words = []
  shortest = len(txt)
  for i in txt:
    i = ''.join(e for e in i.lower() if e.isalnum())
    if i.isdigit() == True:
      pass
    elif len(i) == shortest:
      shortest_words.append(i)
    elif len(i) < shortest:
      del shortest_words[:]
      shortest_words.append(i)
      shortest = len(i)
    else:
      pass
  return sorted(shortest_words)

