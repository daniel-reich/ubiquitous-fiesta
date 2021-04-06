
import re
​
def dakiti(sentence):
  n = re.findall(r'\d+', sentence)
  sentence = sentence.split()
  ans = []
  for i in range(1, len(n) + 1):
    s = sentence[n.index(str(i))]
    s = s.replace(str(i), '')
    ans.append(s)
  return ' '.join(ans)

