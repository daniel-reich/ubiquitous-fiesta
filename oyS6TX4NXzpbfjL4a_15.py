
def best_start(lst, word):
  word = word.upper()
  print("Hi")
  points = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':2,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10} 
  bestScore = 0
  bestIndex = 0
  for i in range(len(lst)-len(word)):
    multiplier = 1
    currentScore = 0
    for j in range(len(word)):
      if lst[i+j] == "DL":
        currentScore += points[word[j]]
      if lst[i+j] == "TL":
        currentScore += points[word[j]]*2
      if lst[i+j] == "DW":
        multiplier += 1
      currentScore += points[word[j]]
    currentScore *= multiplier
    if currentScore > bestScore:
      bestScore = currentScore
      bestIndex = i
  return bestIndex

