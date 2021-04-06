
def sharedLetters(a, b):
  count = ""
  a = a.lower()
  b = b.lower()
  for i in range (len(a)):
    if a[i] in b:
      if a[i] not in count:
        count +=a[i]
  count = ''.join(sorted(count))
  return count

