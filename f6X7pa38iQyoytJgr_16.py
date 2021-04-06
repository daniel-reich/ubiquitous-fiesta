
def increasing_word_weights(sentence):
  x = [[ord(i) for i in n if i.isalpha()] for n in sentence.split(' ')]
  y = [sum(i) for i in x]
  z = [y[i]>y[i-1] for i in range(len(y)) if i !=0]
  return False not in z

