
def max_occur(text):
  str = sorted(set(text),key=text.index)
  cou = [text.count(x) for x in str]
  arr = []
  if all(list(x==1 for x in cou)):
    return "No Repetition"
  else:
    i=0
    while i<len(str):
      if text.count(str[i])==max(cou):
        arr.append(str[i])
      i+=1
    return sorted(arr)

