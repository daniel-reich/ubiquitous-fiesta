
def is_alphabetically_sorted(sentence):
  def is_sorted(word):
    for next_index, letter in enumerate(word[:-1], start=1):
      if letter > word[next_index]:
        return False
    return True
    
  return any(
    is_sorted(word.strip(',.?!'))
    for word in sentence.split()
    if len(word) > 2
  )

