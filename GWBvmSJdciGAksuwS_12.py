
def find_letters(word): 
  new = []
  for i in word:
    count = word.count(i)
    if count ==1:
      new.append(i)
  return new

