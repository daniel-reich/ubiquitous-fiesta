
def vertical_txt(txt):
  w = txt.split()
  r = [[" "for _ in range(len(w))] for _ in range(max(list(map(len, w))))]
  for word in range(len(w)):
    for letter in range(len(w[word])):
      r[letter][word] = w[word][letter]
  return r

