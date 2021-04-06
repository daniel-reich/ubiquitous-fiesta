
import string
def decrypt(lst):
  lst = sorted(lst)
  for i in lst:
    if (lst[i+1] - lst[i])>1:
      x = i+1
      return string.ascii_uppercase[x]

