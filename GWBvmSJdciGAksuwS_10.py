
def find_letters(word):
  lst=[]
  for char in word:
    if word.count(char)==1:
       lst.append(char)
  return lst

