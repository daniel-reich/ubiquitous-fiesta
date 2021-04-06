
def best_start(lst, word):
  points = [1,3,3,2,1,4,2,4,1,8,5,2,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
  lst2 = []
  add = ['-','DL','TL']
  for i in range(16-len(word)):
    p = 0
    multiple = 1
    for j in range(len(word)):
      if lst[i+j] == 'DW':
        p += points[ord(word[j].lower())-97]
        multiple *= 2
      else:
        p += (add.index(lst[i+j])+1)*points[ord(word[j].lower())-97]
    lst2.append(multiple*p)
  return lst2.index(max(lst2))

