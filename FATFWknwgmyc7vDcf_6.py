
import re
​
def subs(m):
  res = m.group(1)+ m.group(2) + m.group(3)+ m.group(4)
  if int(m.group(5)) <= 20:
    res = res + "20" + m.group(5)
  else:
    res = res + "19" + m.group(5)
  return res
​
​
def small_favor(sentence):
  regex = r"(0[1-9]|1[0-9]|2[0-9]|3[0-1])(/|\.)(0[1-9]|1[0-2])(/|\.)([0-9][0-9])" 
  sentence = re.sub(regex,subs,sentence)
  regex = r"(January|February|March|April|May|June|July|August|September|October|November|December)(/|\.|, )(0[1-9]|1[0-9]|2[0-9]|3[0-1])(/|\. )([0-9][0-9])"
  # print(re.search(regex, sentence).group(2))
  return re.sub(regex,subs,sentence)

