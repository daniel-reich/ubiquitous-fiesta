
import string
def count_same_ends(a):
  return sum([i[0] == i[-1] for i in [x.lower().strip(string.punctuation) for x in a.split()]if len(i) > 1] )

