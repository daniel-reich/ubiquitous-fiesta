
def elasticize(word):
  asd = [(a+1)*word[a] if a < (len(word)/2) else (len(word)-a)*word[a] if a >= (len(word)/2) else "!!" for a in range(len(word))]
  return ''.join(asd)

