
def word_search(letters, words):
  horiz = ["".join(row) for row in zip(*[iter(letters.lower())]*8)]
  vert = ["".join(col) for col in zip(*horiz)]
  diag_down = (["".join(horiz[i][x+i] for i in range(8-x)) for x in range(8)[::-1]]
    + ["".join(horiz[y+i][i] for i in range(8-y)) for y in range(1,8)])
  diag_up = (["".join(horiz[y-i][i] for i in range(y+1)) for y in range(8)]
    + ["".join(horiz[7-i][x+i] for i in range(8-x)) for x in range(1,8)])
  
  return all(any(
    word in line or word[::-1] in line
    for list in (horiz,vert,diag_down,diag_up) for line in list
  ) for word in (word.lower() for word in words))

