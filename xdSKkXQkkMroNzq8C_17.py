
def count_d(sentence):
  count = 0
  for x in sentence:
    if 'd' == x or 'D' == x: 
      count = count + 1
  return count

