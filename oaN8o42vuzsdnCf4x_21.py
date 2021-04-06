
def best_words(lst):
  def evaluate(word):
    lookup = {
      1: ['A','E','I','N','O','R','S','T','U'],
      2: ['D','G','L'],
      3: ['B','C','M','P'],
        4: ['F','H','V','W','Y'],
        5: ['K'],
        8: ['J','X'],
        10: ['Q','Z'],
      }
    word = word.upper()
    word_len = len(word)
    score = counted_letters = 0
  
    for key in lookup.keys():
      n = len([ch for ch in word if ch in lookup[key]])
      score += key*n
      counted_letters += n
      if counted_letters == word_len:
        break
    return score
  
  scores = [evaluate(word) for word in lst]
  value = max(scores)
​
  return [lst[i] for i,score in enumerate(scores) if score == value]

