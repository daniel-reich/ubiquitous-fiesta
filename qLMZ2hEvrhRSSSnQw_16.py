
def make_grlex(lst):
  def help(word):
    return (len(word), word)
  
  return sorted(lst, key=help)

