
def is_alphabetically_sorted(sentence):
  b=sentence.strip(".")
  for word in b.split():
    if len(word)>=3:
      a=[]
      for letter in word:
        
        a.append(letter)
      x="".join(sorted(a))
      a=[]
      if x==word:
        return True
  return False

