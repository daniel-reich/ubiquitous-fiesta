
def longest_7segment_word(l):
  l = [i for i in l if all(j not in "kmvwx" for j in i)]
  return max(l, key = len) if l else ""

