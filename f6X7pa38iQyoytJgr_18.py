
def increasing_word_weights(sentence):
  wds = sentence.split()
  weights = []
  for w in wds:
    weight = 0
    for ch in w:
      if ch.isalpha():
        weight += ord(ch)
    weights.append(weight)
  for i in range(len(weights)-1):
    if weights[i] >= weights[i+1]:
      return False
  return True

