
def bird_code(lst):
  import re
  ans = []
  final = []
  for x in lst:
    ans.append(re.split('[\-\s+]',x))
  for x in ans:
    if len(x) == 1:
      a = ''.join(x)
      final.append(a[:4].upper())
    elif len(x) == 2:
      final.append(x[0][:2].upper() + x[1][:2].upper())
    elif len(x) == 3:
      final.append(x[0][0].upper() + x[1][0].upper() + x[2][:2].upper())
    else:
      final.append(x[0][0].upper() + x[1][0].upper() + x[2][0].upper() + x[3][0].upper())
  return final

