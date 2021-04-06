
lp = {
'A':1,
'B':3,
'C':3,
'D':2,
'E':1,
'F':4,
'G':2,
'H':4,
'I':1,
'J':8,
'K':5,
'L':2,
'M':3,
'N':1,
'O':1,
'P':3,
'Q':10,
'R':1,
'S':1,
'T':1,
'U':1,
'V':4,
'W':4,
'X':8,
'Y':4,
'Z':10
}
​
def best_start(lst, word):
  best = {
   'value':0,
   'pos':0
  }
  for i in range(len(lst) - len(word) + 1):
    som = 0
    dw = False
    for j in range(len(word)):
      if lst[i + j] == 'DL':
        som += lp[word[j].upper()] * 2
      elif lst[i + j] == 'TL':
        som += lp[word[j].upper()] * 3
      elif lst[i + j] == 'DW':
        dw = True
        som += lp[word[j].upper()]
      else:
        som += lp[word[j].upper()]
    if dw == True:
      som *= 2
    
    if best['value'] < som:
      best['value'] = som
      best['pos'] = i
  return best['pos']

