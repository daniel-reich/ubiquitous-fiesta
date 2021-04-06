
animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
def fauna_number(txt):
  txt = txt.replace(',', ' ').replace('.', ' ')
  words = txt.split()
  groups = []
  for i,word in enumerate(words):
    if word in animals:
      groups.append((word, words[i-1]))
  return groups

