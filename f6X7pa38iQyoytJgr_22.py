
def increasing_word_weights(sentence):
  lst = [sum([ord(a) for a in w if a.isalpha()])for w in sentence.split()]
  return all([b > a for a, b in zip(lst[::], lst[1::])])

