
def partition(txt, n):
  return [txt[x : x + n] for x in range(0, len(txt),n)]

