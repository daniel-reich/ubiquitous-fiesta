
# 10 Happy Birthday Jack! 10 #
​
def get_birthday_cake(name, age):
  ans = []
  if age % 2 == 0:
    s = '#'
  else:
    s = '*'
  v = s + " " + str(age) + " Happy Birthday " + name + "! " + str(age) + " " + s
  ans.append(s * len(v))
  ans.append(v)
  ans.append(s*len(v))
  return ans

