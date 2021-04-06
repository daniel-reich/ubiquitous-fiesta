
import string
def prime(n):
  lst=[no for no in range(1,n+1) if n%no==0]
  return len(lst)==2
def add(string):
  alphabet="abcdefghijklmnopqrstuvwxyz"
  if string.isdigit():
    value=[int(digit) for digit in string]
    return sum(value)
  else:
    value=[alphabet.index(letter.lower())+1 for letter in string]
    return sum(value)
def sentence_primeness(sentence):
  whitelist=string.ascii_letters+string.digits+" "
  newsentence=""
  for char in sentence:
    if char in whitelist:
      newsentence+=char
    else:
      newsentence+=" "
  new=(newsentence).split(" ")
  result=[add(term) for term in new]
  if prime(sum(result))==True:
    return "Prime Sentence"
  else:
    removal=[i for i in range(len(result)) if prime(sum(result)-result[i])==True]
    if len(removal)==0:
      return "Composite Sentence"
    return "Almost Prime Sentence" +" ("+(new[removal[0]]) +")"

