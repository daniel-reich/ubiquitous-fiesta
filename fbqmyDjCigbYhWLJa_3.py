
def split_into_buckets(phrase, n):
  buckets = []
  words = phrase.split()
  if n < max(map(len, words)):
    return []
  while len(words) > 0:
    bucket = words.pop(0)
    while len(words) > 0 and len(bucket) + len(words[0]) + 1 <= n:
      bucket = bucket + ' ' + words.pop(0)
    buckets.append(bucket)
  return buckets
    
split_into_buckets("a b c d e", 3)

