
def unstretch(word):
  lis = []
  j=0
  for i in range(len(word)):
    if i <= (len(word)-2):
      if word[i]!=word[i+1]:
        lis.append(set(word[j:i+1]))
        j = i+1
      else:
        pass
    else:
      lis.append(set(word[j:]))
  lis = [x for i in lis for x in i]
  return "".join(lis)

