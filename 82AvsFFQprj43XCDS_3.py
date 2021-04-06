
def no_strangers(txt):
  txt_nopunc = ''
  str_punc = '!()-[]{};:"\,<>./?@#$%^&*_~'
  for i in txt:
    if i not in str_punc:
      txt_nopunc += i
  list1 = txt_nopunc.lower().split()
  list2a, list2b = [], []
  dict1 = {}
  for item in list1:
    if item not in dict1.keys():
      dict1[item] = 1
    else:
      dict1[item] += 1
    if dict1[item] >= 3 and dict1[item] < 5 and item not in list2a:
      list2a.append(item)
    elif dict1[item] >=5 and item not in list2b:
      list2b.append(item)
      list2a.remove(item)
  return [list2a, list2b]

