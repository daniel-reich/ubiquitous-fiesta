
import string
​
def count_same_ends(txt):
  lst = "".join(i if i not in string.punctuation else ' ' for i in txt)
  return sum((1 for i in lst.split(' ') if len(i) > 1 and i[0].lower() == i[-1].lower()))

