
scores = {
'A':  1,
'B':  3,
'C':  3,
'D':  2,
'E':  1,
'F':  4,
'G':  2,
'H':  4,
'I':  1,
'J':  8,
'K':  5,
'L':  2,
'M':  3,
'N':  1,
'O':  1,
'P':  3,
'Q':  10,
'R':  1,
'S':  1,
'T':  1,
'U':  1,
'V':  4,
'W':  4,
'X':  8,
'Y':  4,
'Z':  10
}
​
def best_words(lst):
  highestScore = 0
  highestScorers = []
  for w in lst:
    score = 0
    for c in w:
      score += scores[c.upper()]
    if score == highestScore:
      highestScorers.append(w)
    elif score > highestScore:
      highestScore = score
      highestScorers.clear()
      highestScorers.append(w)
  return highestScorers

