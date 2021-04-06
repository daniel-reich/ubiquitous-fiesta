
def edit_words(lst):
  def edit(word):
    word = list(reversed([l8r.upper() for l8r in word]))
    if len(word) % 2 == 0:
      return '-'.join([''.join(word[:len(word)//2]), ''.join(word[len(word)//2:])])
    else:
      return '-'.join([''.join(word[:(len(word)//2)+1]), ''.join(word[(len(word)//2)+1:])])
  
  return [edit(word) for word in lst]

