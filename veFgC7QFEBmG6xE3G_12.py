
def is_smooth(sentence):
  lst = sentence.lower().split()
  return all(lst[a][-1] == lst[a+1][0] for a in range(len(lst)-1))

