
def grant_the_hint(txt):
  txt_array = txt.split(" ")
  max_length = len(max(txt.split(" "), key=len))
  H = list()
  for n in range(max_length+1):
    hint = [word[:n] + '_'*(len(word)-n) for word in txt_array]
    H.append(' '.join(hint))
  return H

