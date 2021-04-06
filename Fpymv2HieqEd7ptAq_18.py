
import re
def split(string):                    # Parentheses clusters
  counter, pattern, index = 0, r'\)\(', []
  for i, x in enumerate(string):
    if i!=len(string)-1:
      if x=="(": counter += 1
      elif x==")": counter -= 1
      if not counter and re.search(pattern, string[i]+string[i+1]): index.append(i)
  string = list(string)
  for x in index: string[x] += " "
  return "".join(string).split()

