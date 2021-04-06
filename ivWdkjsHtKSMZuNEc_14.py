
import string
def find_shortest_words(txt):
  txt=txt.translate(txt.maketrans('', '', string.punctuation))
  lenghts=[len(i) for i in txt.split()]
  return sorted([x.lower() for x,y in zip(txt.split(),lenghts) if y==min(lenghts) and x.isalpha()])

