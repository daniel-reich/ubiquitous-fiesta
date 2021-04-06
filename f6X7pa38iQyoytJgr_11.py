
def increasing_word_weights(sentence):
  a = [sum([ord(i) for i in j if i.isalpha()]) for j in sentence.split()]
  return all([a[i]>a[i-1] for i in range(1,len(a))])

