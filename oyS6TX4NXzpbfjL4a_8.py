
def best_start(lst, word):
  letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 2, 
  3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
  
  arr = []
  for x in word:
    score = 0
    for c in x:
      score += points[letters.index(c.upper())]
    arr.append(score)
    
  DW = sum(arr)*2       # Double word score
  TL = max(arr)*2 + sum(arr)  # Triple letter score
  DTL = max(arr)*2 + (arr[arr.index(max(arr))]+ 4)*2  # Double Triple letter score
  
  if len(word) <= 4:
    #we can only hit one special square
    if DW > TL:
      index = lst.index("DW") #can index get lower?
      while lst[index] == "DW" or lst[index] == '-':
        if index > 0:
          index -= 1
        else : break
      return index
    else : 
      if arr.index(max(arr)) == 0:
        return lst.index("TL")
      else : return lst.index("TL") - arr.index(max(arr))
      
  elif len(word) > 4 and len(word) <= 8:
    #we will utilize TL and DW
    if arr.count(max(arr)) == 1:
      if arr.index(max(arr)) == 0:
        for i in range(len(lst)-1, -1, -1):
          if lst[i] == "TL":
            return i
    else :
      #we will utlize DW and TL
      index = lst.index("DW") #can index get lower?
      while lst[index] == "DW" or lst[index] == '-':
        if index > 0:
          index -= 1
        else : break
      return index

