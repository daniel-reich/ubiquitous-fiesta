
import re
import string
​
def sentence_primeness(sentence):
​
  #functions
  def prime(x):
      if x == 4:
          return False
      for i in range(2, x//2):
          if x % i == 0:
              return False
      return True
​
  #setup
  invalidCharacters = []
  wordValues = []
  lowerCase = list(string.ascii_lowercase)
  lowerCase.insert(0, "")
  upperCase = list(string.ascii_uppercase)
  upperCase.insert(0, "")
  digits = list(string.digits)
​
  #removes every non alphanumeric character
  sentence = re.sub(r"[^a-zA-Z0-9 ]", "", sentence)
​
  #splits string into individual words
  sentence = sentence.split(" ")
​
  #removes unneccessary list items
  while "" in sentence:
      sentence.remove("")
​
  #calculates sentence and word values
  sentenceValue = 0
  for word in sentence:
      wordValue = 0
      for c in word:
          for i in lowerCase:
              if i == c:
                  wordValue += lowerCase.index(i)
          for i in upperCase:
              if i == c:
                  wordValue += upperCase.index(i)
          for i in digits:
              if i == c:
                  wordValue += digits.index(i)
      wordValues.append(wordValue)
      sentenceValue += wordValue
​
  #prime sentence
  if prime(sentenceValue) == True:
      return "Prime Sentence"
​
  #almost prime sentence
  for value in wordValues:
      if prime(sentenceValue - value) == True:
          return "Almost Prime Sentence (" + sentence[wordValues.index(value)] + ")"
​
  #composite sentence
  return "Composite Sentence"

