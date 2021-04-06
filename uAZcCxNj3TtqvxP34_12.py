
def mode(nums):
  dictionaryOfNumbers = {}
  for number in nums:
      if number not in dictionaryOfNumbers:
          dictionaryOfNumbers[number] = 1
      elif number in dictionaryOfNumbers:
          dictionaryOfNumbers[number] += 1
​
  maxValue = max(dictionaryOfNumbers.values())
  modeNumber = [k for k, v in dictionaryOfNumbers.items() if v == maxValue]
  modeNumber.sort()
  return modeNumber

