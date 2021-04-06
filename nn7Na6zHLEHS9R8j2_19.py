
def deep_count(lst):
  from string import punctuation
  text = str(lst)
  trans = str.maketrans('', '', punctuation)
  num_1 = sum([1 for i in text if i is '[']) - 1
  num_2 = len(text.translate(trans).split())
  return num_1 + num_2

