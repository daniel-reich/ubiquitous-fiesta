
def most_common_words(text,n):
  lst = []
  text = text.replace('\n',' ').replace("'"," ").lower()
  text = ''.join([i for i in text if i.isalpha() or i==' ']).split()
  t = list(set(text))
  for i in t:
    lst.append([i,text.count(i)])
  lst = sorted(lst,key=lambda x:x[1])[::-1]
  lengths = [i[1] for i in lst]
  if n<len(lengths):
    lengths = lengths[:n]
  ret = {}
  for i in text:
    if text.count(i) in lengths:
      ret[i] = text.count(i)
    if len(ret)==n:
      return ret
  return ret

