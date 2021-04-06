
def roman_numerals(arg):
  key = (('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1))
  dic = dict(key)
  if type(arg) is str:
    res = 0
    last = 0
    for i in arg:
      res += dic[i] - (last * 2 * (last and last < dic[i]))
      last = dic[i]
    return res
  else:
    res = ''
    for rom, dec in key:
      res += rom * (arg//dec)
      arg %= dec
    for un, fv, tn in (('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M')):
      res = res.replace(fv + un*4, un+tn).replace(un*4, un+fv)
    return res

