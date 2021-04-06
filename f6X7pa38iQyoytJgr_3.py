
def increasing_word_weights(sentence):
  lst = sentence.split()
  weights = []
  for word in lst:
    tot = 0
    for let in word:
      if let.isalpha():
        tot+=ord(let)
    weights.append(tot)
  return weights==sorted(weights)

