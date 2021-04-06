
def join(lst):
  word = ''
  count = []
  for i in range(len(lst)-1):
    word+=lst[i]
    if lst[i][-1] in lst[i+1]:
      l = lst[i+1].index(lst[i][-1])
      if lst[i][-l-1:]==lst[i+1][:l+1]: word=word[:-l-1]
      count.append(l+1)
  word += lst[-1]
  return [word,min(count)] if count else [word,0]

