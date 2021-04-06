
def get_middle(word):
 if len(word)==0:
  return word
 if len(word)%2==0:
  return word[len(word)//2 -1]+ word[len(word)//2]
 return word[len(word)//2]

