
def count_same_ends(txt):
  words = txt.lower().split()
  return sum([(word.rstrip("!.?")[0]==word.rstrip("!.?")[-1] and len(word.rstrip("!.?"))>1) for word in words])

