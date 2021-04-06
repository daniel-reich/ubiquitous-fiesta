
def find_broken_keys(txt1, txt2):
  return [txt1[c] for c in range(len(txt1)) if txt1[c]!=txt2[c] and txt1.index(txt1[c])==c]

