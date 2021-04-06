
def alphabet_index(txt):
  return ' '.join([str(ord(x) - ord('a') + 1) for x in txt.lower() if x.isalpha()])

