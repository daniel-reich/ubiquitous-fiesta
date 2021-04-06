
def is_smooth(sentence):
  lst = sentence.split()
  for i in range(len(lst)-1):
    if lst[i][-1] != lst[i+1][0].lower():
      return False
  return True

