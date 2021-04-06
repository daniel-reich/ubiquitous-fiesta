
def digit_occurrences(start, end, digit):
  l=[str(x) for x in range(start,end+1)]
  s=''
  for x in l:
    s+=x
  return s.count(str(digit))

