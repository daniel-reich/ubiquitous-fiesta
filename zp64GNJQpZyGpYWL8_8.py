
import re
def score_it(s):
  score = 0
  s = re.sub(r'[^\d()]', '', s)
  for match in re.finditer(r'\d+', s):
    num = int(s[match.start():match.end()])
    depth = sum([1 if c == '(' else -1 if c == ')' else 0 for c in s[:match.start()]])
    score += num * depth
  return score

