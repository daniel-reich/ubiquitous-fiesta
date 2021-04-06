
import re
animals = ["muggercrocodile","one-hornedrhino","python","moth","monitorlizard","bengaltiger"]
def fauna_number(txt):
  
  numbers = re.findall(r'\d+',txt)
  words = list(filter(lambda x: x in txt,animals))
  words.sort(key = lambda x: txt.index(x))
  return [(a,b) for a,b in zip(words,numbers)]

