
import itertools
def valid_rondo(s):
  if len(s) == 1:
    return False
  else:
    if s[0] == 'A' and s[-1] == 'A':
      for key,group in itertools.groupby(s):
        if len(list(group)) > 1:
          return False
      return True
    else:
      return False

