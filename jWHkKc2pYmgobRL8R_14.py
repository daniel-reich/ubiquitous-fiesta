
def distance_to_nearest_vowel(txt):
  out, lst =[],[i for i in range(len(txt)) if txt[i].lower() in ['a','e','i','o','u']]
  for i in range (len(txt)):
    out.append(min([abs(i-j) for j in lst]))
  return out

