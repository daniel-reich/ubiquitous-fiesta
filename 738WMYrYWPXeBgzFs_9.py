
def is_valid(txt):
  dic = {}
  for let in txt:
    if not let in dic:
      dic[let] = 0
    dic[let]+=1
  base = min_number(dic)
  error = False
  print(dic)
  for keys in dic:
    if (dic[keys] >= base+2 or (error and dic[keys] == base+1)):
      return "NO"
    else:
      if dic[keys] == base+1:
        error = True
  return "YES"
def min_number(dic):
  min_val = 999
  for keys in dic:
    if dic[keys]<min_val:
      min_val = dic[keys]
  return min_val

