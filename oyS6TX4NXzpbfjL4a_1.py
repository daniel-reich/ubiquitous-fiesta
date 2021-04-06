
def best_start(lst, word):
  return max([calculate_score(lst,word.upper(),i) for i in range(len(lst) - len(word))])[1] * -1
  
def calculate_score(lst,word,start):
  scores = {'A':  1,'B':  3,'C':  3,'D':  2,'E':  1,'F':  4,'G':  2,'H':  4,'I':  1,'J':  8,'K':  5,'L':  2,'M':  3,'N':  1,'O':  1,'P':  3,'Q':  10,'R': 1,'S':  1,'T':  1,'U':  1,'V':  4,'W':  4,'X':  8,'Y':  4,'Z':  10}
  score = 0
  wordmult = 1
  for idx, i in enumerate(word):
    if lst[idx + start] == 'DL':
      score += scores[i] * 2
    elif lst[idx + start] == 'TL':
      score += scores[i] * 3
    elif lst[idx + start] == 'DW':
      score += scores[i]
      wordmult = 2
    else:
      score += scores[i]
  return (score*wordmult,-start)

