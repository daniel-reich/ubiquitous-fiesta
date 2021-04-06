
def get_middle(word):
  middle = len(word) // 2
  if len(word) < 3:
    return word
  if (len(word) % 2 == 1):
    return word[middle]
  else:
    return word[middle-1]+word[middle]

