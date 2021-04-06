
def count_d(sentence):
  count = 0
  for i in range(len(sentence)):
    if sentence[i] == "D" or  sentence[i] == "d":
      count = count + 1
  return count

