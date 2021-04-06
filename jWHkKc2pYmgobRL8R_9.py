
def distance_to_nearest_vowel(txt):
  vowelIndexes = []
  returnList = []
  vowels = ['a','e','i','o','u']
  for i in range(len(txt)): 
    if txt[i] in vowels: 
      vowelIndexes.append(i)
  for i in range(len(txt)):
    broke = False
    if txt[i] not in vowels:
      ranges = []
      for j in vowelIndexes:
        ranges.append(abs(i-j))
      returnList.append(min(ranges))
    else:
      returnList.append(0)
  return returnList

