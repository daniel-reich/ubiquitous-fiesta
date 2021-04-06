
import string
def check_pattern(lst, pattern):
  t = list(string.ascii_uppercase)[0:4]
  al = t[::-1] if pattern[0] != 'A' else t
  result, idx, dic = "", 0, {}
  for e in lst:
    if str(e) not in dic:
      dic[str(e)] = al[idx]
      result += al[idx]
      idx += 1
    else:
      result += dic[str(e)]
  return result == pattern

