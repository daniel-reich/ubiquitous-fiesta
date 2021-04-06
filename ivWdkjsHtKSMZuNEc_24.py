
def find_shortest_words(txt):
  txt=txt.split()
  count=len(txt[1])
  txt[-1]=txt[-1].replace('.','')
  for word in txt:
    for letter in word:
      if letter is ".":
        word.replace('.','')
    if len(word)<count: count=len(word)
  return sorted([word.lower() for word in txt if (len(word)==count and word.isdigit()==False)])

