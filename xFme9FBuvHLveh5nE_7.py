
import itertools
def is_zygodrome(num):
  if len(str(num)) == 2:
    if str(num)[0] == str(num)[1]:
      return True
    else:
      return False
  else:
    num = [x for x in str(num)]
    for key,group in itertools.groupby(num):
      if len(list(group)) >= 2:
        continue
      else:
        return False
    return True

