
import re
def camelCasing(s):
  pattern = '[a-zA-Z]+'
  res = re.findall(pattern, s)
​
  res = [res[i].title() if i != 0 else res[i].lower() for i in range(len(res))]
  return "".join(res)

