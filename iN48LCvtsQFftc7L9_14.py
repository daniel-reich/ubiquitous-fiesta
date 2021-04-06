
def word_search(letters, words):
  horiz = [letters[8*i:(8*i)+8].lower() for i in range(8)]
  vert = [''.join(letters[8*i + j].lower() for i in range(8)) for j in range(8)] 
​
  diagr = []
  diagl = []
  for i in range(15):
    diagr.append('')
    diagl.append('')
    
  for i in range(8):
    for j in range(8):
      diagr[i+j] += horiz[i][j]
      diagl[i+j] += horiz[i][7-j]
​
  for word in words:
    found = False
    wordr = word[::-1]
    found = found or any(word in horiz[i] for i in range(len(horiz)))
    found = found or any(word in vert[i] for i in range(len(vert)))
    found = found or any(word in diagr[i] for i in range(len(diagr)))
    found = found or any(word in diagl[i] for i in range(len(diagl)))
    found = found or any(wordr in horiz[i] for i in range(len(horiz)))
    found = found or any(wordr in vert[i] for i in range(len(vert)))
    found = found or any(wordr in diagr[i] for i in range(len(diagr)))
    found = found or any(wordr in diagl[i] for i in range(len(diagl)))
    if not found:
      return False
  return True

