
def is_alphabetically_sorted(sentence):
  lst = sentence.lower().strip('.').split(' ')
  return True in [list(i) == sorted(i) for i in lst if len(i) > 2]

