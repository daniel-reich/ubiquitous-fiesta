
def factory(n):
  def hmm(lst):
    return [i//n for i in lst]
  return hmm

