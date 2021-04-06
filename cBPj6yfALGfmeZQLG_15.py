
def vertical_txt(txt):
  vert1 = txt.split(' ')
  lenLst = [len(i) for i in vert1]
  longestWord = lenLst.index(max(lenLst))
  vert2 = [[' ' for i in vert1] for i in vert1[longestWord]]
  for worCounter, word in enumerate(vert1):
    for letCounter, letter in enumerate(word):
      vert2[letCounter][worCounter] = letter
  return vert2

