
def dakiti(sentence):
  ordered = []
  for word in sentence.split():
    n,word = int(''.join(i for i in word if i.isdigit())),''.join(i for i in word if not i.isdigit())
    ordered.append((n,word))
  return ' '.join(word[1] for word in sorted(ordered,key=lambda x:x[0]))

