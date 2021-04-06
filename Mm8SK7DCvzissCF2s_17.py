
def in_alpha(word):
  return sum([ord(w.lower())-ord('a')+1 for w in word if w.isalpha()])%2==0

