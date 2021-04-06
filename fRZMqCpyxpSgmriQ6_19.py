
def sorting(s):
  alpha = sorted(set([i.lower() for i in s if i.isalpha()]))
  lower = sorted([i for i in s if i.isalpha() and i.islower()])
  upper = sorted([i for i in s if i.isalpha() and i.isupper()])
  digit = sorted([i for i in s if i.isdigit()])
  lst = []
  for i in alpha:
    if i in lower:
      lst.append(i)
    if i.upper() in upper:
      lst.append(i.upper())
  return ''.join(lst+digit)

