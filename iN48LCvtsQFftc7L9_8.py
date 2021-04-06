
def word_search(letters, words):
  lst = [''] * 8
  for i in range(len(lst)):
    lst[i] = [''] * 8
  it = 0
  letters = letters.lower()
  for i in range(len(lst)):
    for x in range(len(lst[i])):
      lst[i][x] = letters[it]
      it += 1
  rows, cols, rdiag, ldiag = [], [], [], []
  for i in range(len(lst[0])):
    cols.append(''.join([a[i] for a in lst]))
  rows = [''.join(i) for i in lst]
  for i in range(len(lst)):
    for x in range(len(lst[i])):
      rtemp = ''
      ltemp = ''
      for a in range(8):
        if i+a < 8 and x+a < 8:
          rtemp += lst[i+a][x+a]
        if i+a < 8 and x-a >= 0:
          ltemp += lst[i+a][x-a]
      rdiag.append(rtemp)
      ldiag.append(ltemp)
  for i in words:
    if not any([i in a or i[::-1] in a for a in cols]):
      if not any([i in a or i[::-1] in a for a in rows]):
        if not any([i in a or i[::-1] in a for a in rdiag]):
          if not any([i in a or i[::-1] in a for a in ldiag]):
            return False
  return True

