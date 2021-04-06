
def shift_sentence(txt):
  def l8r_shift(w1, w2):
    return w1[0] + w2[1:]
​
  words = txt.split()
  words.append(words[0])
​
  new_words = []
​
  for n in range(len(words) - 1):
    w1 = words[n]
    w2 = words[n+1]
​
    new_words.append(l8r_shift(w1, w2))
  
  new_words_formatted = [new_words[-1]] + new_words[:-1]
​
  return ' '.join(new_words_formatted)

