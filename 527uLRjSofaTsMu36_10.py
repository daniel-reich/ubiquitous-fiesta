
def get_middle(word):
  mid = (len(word)//2)-1
  
  if len(word) % 2:
    return word[mid+1]
  else:
    return word[mid:mid+2]

