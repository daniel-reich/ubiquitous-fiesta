
from string import ascii_lowercase
def findShortestWords(txt):
  lowertxt = txt.lower()
  newstr = ""
  for i in lowertxt:
    if i in ascii_lowercase+" ":
      newstr += i
  sentence = newstr.split(" ")
    
  lengths = []
  wordarr = []
  for words in sentence:
    if words != '':
      lengths.append(len(words))
      wordarr.append(words)
      print(words)
​
  for i in lengths:
    print(i)
    
  lengths, wordarr = zip(*sorted(zip(lengths, wordarr)))
  print(wordarr)
  print(lengths)
  
​
  count = 0
  for i in lengths:
    if i == lengths[0]:
      count += 1
  print(count)
  return(list(wordarr[:count]))

