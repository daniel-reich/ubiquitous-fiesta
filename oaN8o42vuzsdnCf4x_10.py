
def best_words(lst):
  scores = {'A':  1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 2, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R':  1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
  points = []
  word_points = {}
  for word in lst:
    l8rs = list(word)
    p = 0
    for l8r in l8rs:
      point = scores[l8r.upper()]
      p += point
    points.append(p)
    word_points[word] = p
  
  high_points = max(points)
  winners = []
  for word in lst:
    value = word_points[word]
    if value == high_points:
      winners.append(word)
  return winners

