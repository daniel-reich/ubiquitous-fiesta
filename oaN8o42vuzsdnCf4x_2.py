
import re
​
def best_words(lst):
  all_scores = []
  max_score = 0
  my_dict = {"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":5,"L":2,"M":3,"N":1,"O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}
  for word in lst:
    score = 0
    for letter in word:
      score += my_dict[letter.upper()]
    all_scores.append(score)
    if score > max_score:
      max_score = score
  
  result = []
  for idx, i in enumerate(all_scores):
    if i == max_score:
      result.append(lst[idx])
  
  return result

