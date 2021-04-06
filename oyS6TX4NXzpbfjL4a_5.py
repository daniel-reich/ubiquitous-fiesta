
def best_start(lst, word):
  scores = {"A": 1, "B": 3,"C": 3,"D": 2,"E": 1,"F": 4,"G": 2,"H": 4,"I": 1,"J": 8,"K": 5,"L": 2,"M": 3,"N": 1,"O": 1,"P": 3,"Q": 10,"R": 1,"S": 1,"T": 1,"U": 1,"V": 4,"W": 4,"X": 8,"Y": 4,"Z": 10}
  index = 0
  max = -1
​
  for i in range(len(lst)-len(word) + 1):
      score = 0
      doubles = 0
      for j in range(len(word)):
          if lst[i+j] == 'TL':
              score += scores[word[j].upper()] * 3
          else:
              if lst[i+j] == 'DW':
                  doubles += 1
              score += scores[word[j].upper()]
      for j in range(doubles):
          score *= 2
      if score > max:
          max = score
          index = i
  return index

