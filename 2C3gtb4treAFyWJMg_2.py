
from string import ascii_lowercase
import re
​
def polybius(text):
  abc = ascii_lowercase.replace('j','')
  grid = [[str(x) + str(y) for y in range(1,6)] for x in range(1,6)]
  nums = sum(grid, [])
  if re.match('[\d\s]', text):
    words = text.split()
    chars = sum([[w[i:i+2] for i in range(0, len(w), 2)] + [' '] for w in words], [])
    table = dict(zip(nums, abc))
    return ''.join(map(lambda x: table[x] if x != ' ' else x, chars[:-1]))  
  else:
    text = re.sub('[^a-z\s]', '', text.lower().replace('j','i'))
    table = dict(zip(abc, nums))
    return ''.join(map(lambda x: table[x] if x != ' ' else x, text))

