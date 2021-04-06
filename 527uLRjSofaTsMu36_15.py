
def get_middle(word):
  l = len(word)
  mid = l//2
  if l % 2 == 0:
    return word[mid-1:mid+1]
  else:
    return word[mid]

