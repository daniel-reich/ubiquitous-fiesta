
import re 
​
def find_longest(sentence):
  sentence = re.sub(r'[^A-Za-z ]+', ' ', sentence).lower()
  result = ""
  for i in sentence.split(' '):
    result = i if len(result) < len(i) else result
  return result

