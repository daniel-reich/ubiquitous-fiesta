
def same_letter_pattern(txt1, txt2):
  d = {}
  for i in range(len(txt1)):
    if txt1[i] not in d:
      d[txt1[i]] = txt2[i]
  return ''.join(d[k] for k in txt1)==txt2

