
def split_into_buckets(text, n):
  words = text.split(' ')[::-1]
  buckets = []
​
  if list(x for x in words if len(x) > n):
    return []
  while words:
    for i in range(0,len(words)):
      if len(' '.join(words[i:])) <= n:
        buckets.append(' '.join(words[i:][::-1]))
        words = words[:i]
        break
  return buckets

