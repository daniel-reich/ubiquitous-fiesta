
import string
def find_shortest_words(txt):
  a=txt.translate(str.maketrans('', '', string.punctuation))
  a=a.split()
  b=a
  small=20
  for i in a:
    if len(i)<small:
      small=len(i)
  return sorted([word.lower() for word in a if len(word)==small and not word.isnumeric()])

