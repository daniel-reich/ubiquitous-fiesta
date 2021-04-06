
import re
def numbers_need_friends_too(n):
  n = str(n)
  subs = [pair[0] for pair in re.findall(r"((\d)\2*)", n)]
  result = []
  for sub in subs:
    if len(sub) == 1:
      result.append(sub*3)
    else:
      result.append(sub)
  return int("".join(result))

