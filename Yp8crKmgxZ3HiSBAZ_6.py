
def freq_count(lst, el):
  level, out, passed= 0, [], []
  for i in str(lst):
    if i == '[':
      level+=1
      if len(out) < level:
        out.append(0)
    elif i == ']':
      level -=1
    elif i.isnumeric():
      if float(i) == float(el):
        out[level-1]+=1
  return [[i,out[i]] for i in range (len(out))]

