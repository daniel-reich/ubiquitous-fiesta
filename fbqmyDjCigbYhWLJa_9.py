
def split_into_buckets(phrase, n):
  words = phrase.split()
  bucket = []
  i = 0
  while i < len(words):
    phrase = words[i]
    if n >= len(phrase):
      while 1:
        try:
          if n > len(phrase) + len(words[i+1]):
            phrase += " " + words[i+1]
            i += 1
          else:
            break
        except:
          break
      bucket.append(phrase)
    i+=1
  count = 0
  for b in bucket:
    count += len(b)
  if count < len(phrase):
    return []
  return bucket

