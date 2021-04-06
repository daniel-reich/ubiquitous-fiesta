
def words_to_sentence(w):
  if w==['']or w==[]or w==None:
    return''
  if''in w:
    w.pop(w.index(''))
  if len(w)<2:
    return w[0]
  return' '.join([', '.join(w[0:-1]),'and',w[-1]])

