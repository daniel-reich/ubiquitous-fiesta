
letters = {
  "a": 1,
  "b": 3,
  "c": 3,
  "d": 2,
  "e": 1,
  "f": 4,
  "g": 2,
  "h": 4,
  "i": 1,
  "j": 8,
  "k": 5,
  "l": 1,
  "m": 3,
  "n": 1,
  "o": 1,
  "p": 3,
  "q": 10,
  "r": 1,
  "s": 1,
  "t": 1,
  "u": 1,
  "v": 4,
  "w": 4,
  "x": 8,
  "y": 4,
  "z": 10
  }
​
def checkChunk(lst, start, end, word):
  scoreChunk, splitWord, score, dub = [], list(word.lower()), 0, False
  for i in range(start, end): scoreChunk.append(lst[i])
  for i in range(len(scoreChunk)):
    if (scoreChunk[i]=="-"):
        score+=letters[splitWord[i]]
    elif (scoreChunk[i]=="DL"):
        score+=letters[splitWord[i]]*2
    elif (scoreChunk[i]=="TL"):
        score+=letters[splitWord[i]]*3
    elif (scoreChunk[i]=="DW"):
        dub=True
        score+=letters[splitWord[i]]
  if (dub): score*=2
  return score
​
def best_start(lst, word):
  totals = []
  for i in range(len(lst)-len(word)):
    totals.append(checkChunk(lst, i, i+len(word), word))
  return totals.index(max(totals))

