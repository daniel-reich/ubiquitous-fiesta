
import re
def recur_index(txt):
  try:
    def second(char):
      return [match.start() for match in re.finditer(char, txt)]
    letters = list(filter(lambda x: txt.count(x) >= 2, set(txt)))
    indices = sorted(list(map(lambda x: second(x)[1],letters)))
    i = indices[0]
    return {txt[i]:[txt.index(txt[i]),i]}
  except IndexError:
    return {}
  except TypeError:
    return {}

