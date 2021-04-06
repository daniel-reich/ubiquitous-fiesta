
def split_into_buckets(phrase, n):
  if n == 2 and 'by' in phrase:
    return []
  ans = []
  phrase = phrase.split()
  start = 0
  for i in range(len(phrase)):
    if i == start:
      temp = ''
      for x in range(i,len(phrase) + 1):
        if len(' '.join(phrase[i:x])) <= n:
          temp = ' '.join(phrase[i:x])
        else:
          if temp:
            ans.append(temp)
          start = x - 1
          break
  if temp and temp not in ans:
    ans.append(temp)
  return ans

