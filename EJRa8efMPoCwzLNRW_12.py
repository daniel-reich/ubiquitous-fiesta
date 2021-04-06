
def dakiti(sentence):
  split_charas = lambda wrd: (int([w for w in wrd if w.isdigit()][0]), ''.join([w for w in wrd if not w.isdigit()]))
  word_order = [split_charas(word) for word in sentence.split(' ')]
  sorted_lyrics = [word[1] for word in sorted(word_order, key=lambda w: w[0])]
  return ' '.join(sorted_lyrics)

