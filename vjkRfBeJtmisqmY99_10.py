
def word3(w1,w2,w3):
  if w3 == w1 or w3 == w2:
    return False
  return w2[0]==w3[0] and w3[4] == w1[2]
def word4(w1,w2,w3,w4):
  if w4 == w1 or w4 == w2 or w4 == w3:
    return False
  return w4[2] == w2[4] and w1[6] == w4[6]
def word5(w1,w2,w3,w4,w5):
  if w1 == w5 or w2 == w5 or w3 == w5 or w4 == w5:
    return False
  return w4[0] == w5[0] and w5[4] == w3[2] and w5[6] == w1[0]
def word6(w1,w2,w3,w4,w5,w6):
  if w1 == w6 or w2 == w6 or w3 == w6 or w4 == w6 or w5 == w6:
    return False
  return w6[0] == w2[6] and w6[2] == w4[4] and w6[6] == w3[6] 
def fit_words(words, clue):
  path = []
  for w1 in words:
    for w2 in list(filter(lambda x: x != w1,words)):
      for w3 in list(filter(lambda x: x[3] == clue[1] and word3(w1,w2,x),words)):
        for w4 in list(filter(lambda x: word4(w1,w2,w3,x),words)):
          for w5 in list(filter(lambda x: word5(w1,w2,w3,w4,x),words)):
            for w6 in list(filter(lambda x: word6(w1,w2,w3,w4,w5,x),words)):
              path.append([w1,w2,w3,w4,w5,w6])
  return path[0]

